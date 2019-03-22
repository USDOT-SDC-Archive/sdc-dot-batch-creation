from lambdas.create_batch_lambda_handler import *

def lambda_handler(event, context):
    create_batch_handle_event = CreateBatches()
    create_batch_handle_event.create_batch(event, context)