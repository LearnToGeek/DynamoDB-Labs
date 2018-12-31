from __future__ import print_function
import boto3

dynamoClient = boto3.resource('dynamodb',region_name='us-east-1')

table = dynamoClient.create_table(
    TableName='Membership',
    KeySchema=[
        {
            'AttributeName':'MembershipId',
            'KeyType':'HASH' #Partition Key
        },
        {
            'AttributeName':'MembershipType',
            'KeyType':'RANGE' # Sort Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName':'MembershipId',
            'AttributeType':'S'
        },
        {
            'AttributeName':'MembershipType',
            'AttributeType':'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits':10,
        'WriteCapacityUnits':10
    }
)

print("Table Status : ",table.table_status)