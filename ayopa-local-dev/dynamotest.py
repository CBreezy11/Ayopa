import boto3

ACCESS_KEY = '123'
SECRET_KEY = 'abc'

class PythonAws:
    def __init__(self):
        self.client = boto3.resource('dynamodb',
                                endpoint_url="http://localhost:4569",
                                use_ssl=False,
                                aws_access_key_id=ACCESS_KEY,
                                aws_secret_access_key=SECRET_KEY,
                                region_name='us-east-1')
        self.table = self.client.Table('Ayopa')
    
    def create_table(self):
        self.client.create_table(
            AttributeDefinitions=[
            {
                'AttributeName': 'Data',
                'AttributeType': 'S',
            },
            ],
        KeySchema=[
            {
                'AttributeName': 'Data',
                'KeyType': 'HASH',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        TableName='Ayopa',
        )

    def put_item(self):
        self.table.put_item(
            Item={
            'Data': 'this is the entry',
            'extra': 'the extra data',
            }
        )

    def get_item(self):
        response = self.table.get_item(
            Key={
                'Data': 'this is the entry'
            }
        )
        item = response['Item']
        print(item)
        

