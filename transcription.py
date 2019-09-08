from __future__ import print_function
import time
import boto3
import pprint
import requests
import json

bucket_name = 'handspoken'

s3_client = boto3.client('s3')
transcribe = boto3.client('transcribe')
s3_resources = boto3.resource('s3')

def transcribe_audio(filename, job_name):
    s3_client.upload_file(filename, bucket_name, filename)
    
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': 'https://handspoken.s3.us-east-2.amazonaws.com/' + filename
        },
        OutputBucketName=bucket_name,
    )

def get_text(job_name):
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    # pprint.pprint(status)
    obj = s3_resources.Bucket(bucket_name).Object(job_name + ".json").download_file(job_name + ".json")
    input_file=open(job_name + ".json", 'r')
    transcription = json.load(input_file)
    text = transcription['results']['transcripts'][0]['transcript']
    return text

transcribe_audio('transcribe-sample.mp3',"test4")
print(get_text('test4'))