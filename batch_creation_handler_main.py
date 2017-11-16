from lambdas.batch_creation_lambda_handler import *

def lambda_handler(event, context):
    batch_creation_handle_event = CreateBatches()
    batch_creation_handle_event.create_batch(event, context)