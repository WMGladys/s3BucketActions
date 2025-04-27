import boto3

def list_s3_buckets_and_count_objects():
    """
    Lists all S3 buckets in the AWS account and displays the total number of objects in each bucket.

    This script assumes the EC2 instance has an IAM role with appropriate S3 permissions
    (e.g., AmazonS3ReadOnlyAccess or a custom policy allowing s3:ListBucket and s3:GetObject).
    """
    try:
        # Create an S3 client using boto3.
        # Boto3 will automatically use the IAM role attached to the EC2 instance
        # for authentication and authorization.
        s3_client = boto3.client('s3')

        # List all S3 buckets in the account.
        response = s3_client.list_buckets()
        buckets = response.get('Buckets', [])

        if not buckets:
            print("No S3 buckets found in your account.")
            return

        print("Listing S3 Buckets and their object counts:")
        for bucket in buckets:
            bucket_name = bucket['Name']
            object_count = 0

            # Create an S3 resource client to easily paginate through objects.
            s3_resource = boto3.resource('s3')
            bucket_resource = s3_resource.Bucket(bucket_name)

            # List all objects in the current bucket.
            # For large buckets, this will automatically handle pagination.
            for obj in bucket_resource.objects.all():
                object_count += 1

            print(f"- Bucket Name: {bucket_name}, Total Objects: {object_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_s3_buckets_and_count_objects()
