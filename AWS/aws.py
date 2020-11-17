import boto3

def create_folder(bucket, directory_name):
    try:
        s3 = boto3.client('s3')

        key = directory_name + '/'
        s3.put_object(Bucket=bucket, Key=key)

        return key
    
    except Exception as err:
        print(err)

def upload_image(bucket, mediafile_key, file):
    try:
        s3 = boto3.resource('s3')

        bucket = s3.Bucket(bucket)

        return bucket.put_object(
            ACL='public-read',
            Key=mediafile_key,
            ContentType=file.content_type,
            Body=file
        )

    except Exception as err:
        print(err)

def rename_file(bucket, new_mediafile_key, old_mediafile_key):
    try:
        s3 = boto3.resource('s3')

        s3.Object(bucket, new_mediafile_key).copy_from(CopySource=bucket + '/' + old_mediafile_key)
        s3.Object(bucket, old_mediafile_key).delete()

        s3.Object(bucket, new_mediafile_key).Acl().put(ACL='public-read')

        return True

    except Exception as err:
        print(err)

def delete_mediafile(bucket, mediafile_key):
    try:
        s3 = boto3.resource('s3')
        s3.Object(bucket, mediafile_key).delete()

        return True

    except Exception as err:
        print(err)

def get_mediafile_content(bucket, mediafile_key):
    try:
        s3 = boto3.client('s3')

        data = s3.get_object(Bucket=bucket, Key=mediafile_key)
        return data['Body'].read()

    except Exception as err:
        print(err)

def download_file(bucket, mediafile_key, local_path):
    try:
        s3 = boto3.client('s3')

        with open(local_path, 'wb') as file:
            s3.download_fileobj(bucket, mediafile_key, file)

    except Exception as err:
        print(err)