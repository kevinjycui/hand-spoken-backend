from __future__ import print_function
import time
import boto3
import pprint
import requests
import json

bucket_name = 'handspoken'

# Create an S3 client
s3_client = boto3.client('s3')

filename = 'transcribe-sample.mp3'


# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3_client.upload_file(filename, bucket_name, filename)

###

transcribe = boto3.client('transcribe')
job_name = "test2"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    LanguageCode='en-US',
    MediaFormat='mp3',
    Media={
        'MediaFileUri': 'https://handspoken.s3.us-east-2.amazonaws.com/' + filename
    },
    OutputBucketName='handspoken',
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
pprint.pprint(status)

s3_resources = boto3.resource('s3')
obj = s3_resources.Bucket('handspoken').Object(job_name + ".json").download_file(job_name + ".json")
input_file=open(job_name + ".json", 'r')
transcription = json.load(input_file)
text = transcription['results']['transcripts'][0]['transcript']
print(text)