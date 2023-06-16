import boto3
import json
import argparse

# Arguments
parser = argparse.ArgumentParser(description='Provides translation between one source language and another of the same set of languages.')
parser.add_argument(
    '--file',
    dest='filename',
    help='The path to the input file. The file should be valid json',
    required=True)
    
args = parser.parse_args()

# Function
def open_input():
   # ""This function returns a dictionary containing the contents of the Input section in the input file""
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']
    
def translate_text(**kwargs):
    translate = boto3.client('translate')
    response = translate.translate_text(**kwargs)
    print(response['TranslatedText'])
    
# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    for item in input_text: # Here we iterate over all dictionaries in the Input list
        translate_text(**item)

# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)
    
def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

    
# Main Function - used to call other functions
def main():
    new_input_text_list()
   # translate_loop()
    new_list_comprehension()

    
if __name__ == '__main__':
    main()
    