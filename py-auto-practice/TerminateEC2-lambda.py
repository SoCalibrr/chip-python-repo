import boto3
import datetime

#####
# First function will try to filter for EC2 instances that contain a tag named 'TerminationDate' which is set to '{Today's Date}'
# If that condition is met, function will compare current date (YYYY-MM-DD) to the value of the 'TerminationDate' tag.
# Value of the 'TerminationDate' tag must be in the following format 'YYYY-MM-DD' - Example : '2021-04-29'  
# 
# In order to trigger this function make sure to setup a CloudWatch event which will be executed every day. 
# The following Lambda Function needs a role with permission to terminate EC2 instances and write to CloudWatch logs.
# 
# Example EC2 Instance tags: 
# 
# TerminationDate: 2021-04-29
#####


#define boto3 connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    # Get current time in format H:M
    current_date = datetime.date.today().isoformat()
    
    # Find all the instances that are tagged with TerminationDate: {Today's Date}
    filters = [
        {
            'Name': 'tag:TerminationDate',
            'Values': [current_date]
        }
    ]

    # Search all the instances which contains scheduled filter 
    instances = ec2.instances.filter(Filters=filters)

    terminate_instances = []     

    # Locate all instances that are tagged to start or stop.
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == 'TerminationDate':
                if tag['Value'] == current_date:
                    terminate_instances.append(instance.id)
                    pass
                pass

    print(current_date)
    
    # shut down all instances tagged to stop. 
    if len(terminate_instances) > 0:
        # perform the shutdown
        terminate = ec2.instances.filter(InstanceIds=terminate_instances).terminate()
        terminate   # ??? Is this enough to call the terminate() method ???
    else:
        print("No instances to terminate.")


 # Delete any tags that are older than the current date too
 # How will cloud watch event format the date time. Do I need to use regex?
    # No, right? We're not worried about time of CW event, we just need a trigger

