import boto3

def translate_text(**kwargs):
    translate = boto3.client('translate')
    response = translate.translate_text(**kwargs)
    print(response)

text = input('Provide the text you want translated: ')
source_language_code = input('Provide the 2 letter source language code: ')
target_language_code = input('Provide the 2 letter target language code: ')

def main():
   translate_text(
       Text=text,
       SourceLanguageCode=source_language_code,
       TargetLanguageCode=target_language_code
       )
    
if __name__ == '__main__':
    main()