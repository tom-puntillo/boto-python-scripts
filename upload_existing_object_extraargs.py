import boto3

s3 = boto3.client('s3')


#with open('another_text_file.txt', 'rb') as f:
 #   s3.put_object(Bucket = 'tpuntillo-boto3-06122023', Key = 'test_text.txt', Body = f, ContentType = 'text/plain')
 
s3.upload_file('another_text_file.txt', 'tpuntillo-boto3-06122023', 'another_text_file_upload.txt', ExtraArgs = {'ContentType' : 'text/plain'})
