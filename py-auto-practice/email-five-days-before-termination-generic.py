import json
import boto3
import datetime

def lambda_handler(event, context):
    
    ec2 = boto3.resource('ec2')
    client = boto3.client('ses')

    # Get current time + 5 days in format YYYY-MM-DD
    five_days_after_current_date = (datetime.date.today() + datetime.timedelta(days=5)).isoformat()  # converts the datetime to the iso standard format (YYYY-MM-DD)

    filters = [
        {
            'Name': 'tag:TerminationDate',
            'Values': [five_days_after_current_date]
        }
    ]

    # Search all the instances which contains scheduled filter 
    instances = ec2.instances.filter(Filters=filters)

    email_instances = []     

    # Locate all instances that are tagged to terminate and see if their tag value is 5 days from today.
    # If so, add their Name tag values to the email_instances list
    for instance in instances:
        instance_term_date = None
        tag_name = None
        for tag in instance.tags:
            if tag['Key'] == 'TerminationDate':
                instance_term_date = tag['Value']
            if tag['Key'] == 'Name':
                tag_name = tag['Value']
        
        if tag_name == None:
            tag_name = instance.id
        
        print('Checking instance ' + str(instance.id) + ". Name value is: " + str(tag_name))

        if instance_term_date == five_days_after_current_date:
            # email_instances.append(instance.id)
            email_instances.append(tag_name)
            print(f'{tag_name} is due to be terminated in five days. Added to email_instances list.')
            
    # Send an email that contains the names all of the instances in the email_instances list to the destination address
    if len(email_instances) > 0:
        # instance_list = print(*email_instances, sep = "\n")
        len_instance_list = print(len(email_instances))
        # subject = (str(len_instance_list) + " instances will be terminated in 5 days.")
        subject = ("The Below Lab Manager Instances Will Be Terminated In 5 Days.")
        body = f"""
        <br>
        Hello,
        <br>
        This notification is a courtesy to let you know that {email_instances} will be deleted in five days.
        <br>
        Thanks!
        """
        message = {"Subject" : {"Data" : subject}, "Body" : {"Html" : {"Data" : body}}}
        response = client.send_email(Source = "devops@cbord.com", Destination = {"ToAddresses" : ["ctw2@cbord.com"]}, Message = message)
    else:
        print("No instances will be terminated in five days.")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    # help(string.join)