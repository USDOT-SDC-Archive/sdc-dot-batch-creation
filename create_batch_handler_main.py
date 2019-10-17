from lambdas.create_batch_lambda_handler import *

def lambda_handler(*args, **kwargs):
    create_batch_handle_event = CreateBatches()
    create_batch_handle_event.create_batch()