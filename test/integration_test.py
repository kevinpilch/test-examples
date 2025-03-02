import pytest
import boto3
import json
from io import BytesIO
from minio import Minio
from src.utils.s3_client import S3Client
from src.main import process_costs_s3

TEST_BUCKET = "test-bucket"
INPUT_KEY = "input/costs.json"
OUTPUT_KEY = "output/result.json"

@pytest.fixture(scope="session")
def minio_client():
    """Create a MinIO client for bucket setup"""
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    return client

@pytest.fixture(scope="session")
def s3_client():
    """Create boto3 S3 client configured for MinIO"""
    return S3Client(
        endpoint_url="http://localhost:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin"
    )

@pytest.fixture(scope="function")
def test_bucket(minio_client):
    """Create and clean up test bucket"""
    # Create bucket
    if not minio_client.bucket_exists(TEST_BUCKET):
        minio_client.make_bucket(TEST_BUCKET)
    
    yield TEST_BUCKET
    
    # Cleanup
    try:
        objects = minio_client.list_objects(TEST_BUCKET)
        for obj in objects:
            minio_client.remove_object(TEST_BUCKET, obj.object_name)
        minio_client.remove_bucket(TEST_BUCKET)
    except:
        pass

def test_process_costs_s3_integration(s3_client, test_bucket, minio_client):
    """Test the entire S3 processing workflow"""
    # Prepare test data
    test_data = [
        {"type": "cost", "cost": 100},
        {"type": "cost", "cost": 200},
        {"type": "other", "cost": 300}
    ]
    
    # Convert data to bytes and create a BytesIO object
    data_bytes = json.dumps(test_data).encode('utf-8')
    data_stream = BytesIO(data_bytes)
    
    # Upload test data to MinIO
    minio_client.put_object(
        test_bucket,
        INPUT_KEY,
        data_stream,
        len(data_bytes)  # Length of the data in bytes
    )
    
    # Process the data
    total_cost = process_costs_s3(
        s3_client,
        test_bucket,
        INPUT_KEY,
        test_bucket,
        OUTPUT_KEY
    )
    
    # Verify the result
    assert total_cost == 300
    
    # Check the output file
    result_obj = minio_client.get_object(test_bucket, OUTPUT_KEY)
    result_data = json.loads(result_obj.read().decode('utf-8'))
    assert result_data["total_cost"] == 300 