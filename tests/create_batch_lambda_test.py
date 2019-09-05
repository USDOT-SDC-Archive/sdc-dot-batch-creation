from moto import mock_ssm, mock_sqs, mock_events
import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lambdas.create_batch_lambda_handler import *

latest_batch_id = "devLatestBatchId"


@mock_ssm
def test_get_latest_batch_id():
    ssm = boto3.client('ssm', region_name='us-east-1')
    new_batch_id = str(int(time.time()))
    response = ssm.put_parameter(Name=latest_batch_id, Value=new_batch_id, Type='String')
    assert response != ""
    get_batch_obj = CreateBatches()
    current_batch_id = get_batch_obj.get_latest_batch(latest_batch_id)
    assert current_batch_id == new_batch_id


@mock_ssm
def test_get_latest_batch_id_raise_exception():
    with pytest.raises(Exception):
        ssm = boto3.client('ssm', region_name='us-east-1')
        new_batch_id = str(int(time.time()))
        response = ssm.put_parameter(Name=latest_batch_id, Value=new_batch_id, Type='String')
        assert response != ""
        get_batch_obj = CreateBatches()
        get_batch_obj.get_latest_batch(None)



@mock_ssm
def test_create_new_batch_id():
    generated_batch_id = str(int(time.time()))
    create_batch_obj = CreateBatches()
    new_batch_id = create_batch_obj.create_new_batch_id(latest_batch_id)
    assert generated_batch_id == new_batch_id
    assert new_batch_id.isnumeric()


@mock_ssm
def test_create_new_batch_id_raises_exception():
    with pytest.raises(Exception):
        create_batch_obj = CreateBatches()
        new_batch_id = create_batch_obj.create_new_batch_id(None)


@mock_sqs
def test_push_batchid_to_queue_raises_exception():
    with pytest.raises(Exception):
        sqs = boto3.client('sqs', region_name='us-east-1')
        sqs.create_queue(QueueName='dev-dot-sdc-curated-batches.fifo',
                                    Attributes={'FifoQueue': "true", 'DelaySeconds': "5", 'MaximumMessageSize': "262144",
                                                'MessageRetentionPeriod': "1209600", 'VisibilityTimeout': "960",
                                                'ContentBasedDeduplication': "true"})
        generated_batch_id = str(int(time.time()))
        push_message_obj = CreateBatches()
        push_message_obj.push_batchid_to_queue(generated_batch_id)


@mock_sqs
def test_push_batchid_to_queue():
    sqs = boto3.client('sqs', region_name='us-east-1')
    response = sqs.create_queue(QueueName='dev-dot-sdc-curated-batches.fifo',
                                Attributes={'FifoQueue': "true", 'DelaySeconds': "5", 'MaximumMessageSize': "262144",
                                            'MessageRetentionPeriod': "1209600", 'VisibilityTimeout': "960",
                                            'ContentBasedDeduplication': "true"})
    queue_url = response['QueueUrl']

    queue_name = queue_url[queue_url.rfind('/') + 1: len(queue_url)]
    os.environ['SQS_CURATED_BATCHES_QUEUE_ARN'] = "arn:aws:sqs:us-east-1::"+queue_name
    generated_batch_id = str(int(time.time()))
    push_message_obj = CreateBatches()
    push_message_obj.push_batchid_to_queue(generated_batch_id)
    assert True


@mock_events
def test_create_batch():
    with pytest.raises(Exception):
        os.environ["LATEST_BATCH_ID"] = latest_batch_id
        assert CreateBatches().create_batch(None, None) is None


@mock_events
def test_create_batch_current_batch_id_empty_string():
    os.environ["LATEST_BATCH_ID"] = latest_batch_id

    def mock_get_latest_batch(*args, **kwargs):
        return ""

    def mock_create_new_batch_id(*args, **kwargs):
        return "new_batch_id"

    create_batches = CreateBatches()
    create_batches.get_latest_batch = mock_get_latest_batch
    create_batches.create_new_batch_id = mock_create_new_batch_id

    create_batches.create_batch(None, None)


def test_create_batch_current_batch_id_not_empty_string():

    dict1 = {"x": 0}

    os.environ["LATEST_BATCH_ID"] = latest_batch_id

    def mock_get_latest_batch(*args, **kwargs):
        return "latest_batch_id"

    def mock_push_batchid_to_queue(*args, **kwargs):
        pass

    def mock_create_new_batch_id(*args, **kwargs):
        return "new_batch_id"

    create_batches = CreateBatches()
    create_batches.get_latest_batch = mock_get_latest_batch
    create_batches.push_batchid_to_queue = mock_push_batchid_to_queue
    create_batches.create_new_batch_id = mock_create_new_batch_id

    create_batches.create_batch(None, None)
