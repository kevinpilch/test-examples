import boto3
from typing import Optional

class S3Client:
    """Client for interacting with S3/MinIO storage"""
    
    def __init__(
        self, 
        endpoint_url: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None
    ):
        """
        Initialize S3 client
        
        Args:
            endpoint_url: Optional endpoint URL for MinIO/custom S3 endpoint
            aws_access_key_id: AWS/MinIO access key ID
            aws_secret_access_key: AWS/MinIO secret access key
        """
        self.s3 = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            # Required for MinIO
            aws_session_token=None,
            region_name='us-east-1'  # Doesn't matter for MinIO but required
        )
    
    def read_from_s3(self, bucket: str, key: str) -> str:
        """
        Read file contents from S3
        
        Args:
            bucket: S3 bucket name
            key: Object key in the bucket
            
        Returns:
            str: Contents of the file
        """
        response = self.s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    
    def write_to_s3(self, bucket: str, key: str, data: str) -> None:
        """
        Write data to S3
        
        Args:
            bucket: S3 bucket name
            key: Object key in the bucket
            data: String data to write
        """
        self.s3.put_object(Bucket=bucket, Key=key, Body=data) 