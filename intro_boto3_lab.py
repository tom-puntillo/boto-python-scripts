import boto3

translate = boto3.client('translate')

response = translate.translate_text(
    Text='This is a string',
    SourceLanguageCode='en',
    TargetLanguageCode='fr',
)

print(response)