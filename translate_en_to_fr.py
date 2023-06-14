import boto3

def translate_text(**kwargs):
    translate = boto3.client('translate')
    response = translate.translate_text(**kwargs)
    print(response)

kwargs = {
    'Text' : 'Never give up, never surrender',
    'SourceLanguageCode' : 'en',
    'TargetLanguageCode' : 'fr'
}

def main():
    translate_text(**kwargs)
    
if __name__ == '__main__':
    main()