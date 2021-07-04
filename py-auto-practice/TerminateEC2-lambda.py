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
    
    # Get current time in format YYYY-MM-DD
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

    # Locate all instances that are tagged to terminate.
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == 'TerminationDate':
                if tag['Value'] == current_date:
                    terminate_instances.append(instance.id)

    print(f"Searching for instances with a TerminationDate tag value of: {current_date}.")
    
    # Terminate all instances with TerminateDate values of todays's date. 
    if len(terminate_instances) > 0:
        # perform the termination
        terminate = ec2.instances.filter(InstanceIds=terminate_instances).terminate()
        terminate   
        print(f"The following instances were found and have been terminated: {terminate_instances}.")
    else:
        print("No instances to terminate.")