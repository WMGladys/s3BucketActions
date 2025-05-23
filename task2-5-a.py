import boto3

def list_s3_buckets_and_count_objects():
    try:
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
            for obj in bucket_resource.objects.all():
                object_count += 1

            print(f"- Bucket Name: {bucket_name}, Total Objects: {object_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_s3_buckets_and_count_objects()
