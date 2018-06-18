from common.logger_utility import *
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import uuid


class CreateBatches:
    pass

    def __get_current_batch_id(self, table_name):
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(table_name)
            response = table.scan(
                FilterExpression=Attr('IsCurrent').eq('true')
            )

            if response['Count'] == 0:
                batch_id = ""
            else:
                for item in response['Items']:
                    batch_id = item['BatchId']
            LoggerUtility.logInfo("Current batch id - {}".format(batch_id))
        except Exception as e:
            LoggerUtility.logError("Unable to fetch the records from table - {}".format(table_name))
            raise e
        return batch_id

    def __create_new_batch_id(self, table_name):
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(table_name)
            response = table.put_item(
                Item={
                    "BatchId": str(int(time.time())),
                    "IsCurrent": "true",
                    "ReadyForProcessing": "false"
                }
            )
            LoggerUtility.logInfo("Successfully created a new batch - {}".format(response))
        except Exception as e:
            LoggerUtility.logError("Failed to create a new batch")
            raise e

    def __update_batch_details(self, table_name, batch_id):
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(table_name)
            response = table.update_item(
                Key={
                    "BatchId": batch_id
                },
                UpdateExpression="set IsCurrent = :c, ReadyForProcessing = :r",
                ExpressionAttributeValues={
                    ':c': "false",
                    ':r': "true"
                }
            )
            LoggerUtility.logInfo("Update item response - {}".format(response))
            LoggerUtility.logInfo("Successfully updated batch with id - {}".format(batch_id))
        except Exception as e:
            LoggerUtility.logError("Failed to update the batch id - {}".format(batch_id))
            raise e

    def create_batch(self, event, context):
        LoggerUtility.setLevel()
        LoggerUtility.logInfo("Initiating batch creation process")
        table_name = os.environ['DDB_BATCH_TABLE_ARN'].split('/')[1]
        batch_id = self.__get_current_batch_id(table_name)
        if "" == batch_id:
            self.__create_new_batch_id(table_name)
        else:
            self.__create_new_batch_id(table_name)
            self.__update_batch_details(table_name, batch_id)

        LoggerUtility.logInfo("Completed batch creation process")
