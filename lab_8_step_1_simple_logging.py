# Import logging
import logging
import json

# This uses json string as an inout
json_string = """
{
    "Input":[
        {
            "Text":"I am learning code in AWS",
            "SourceLanguageCode":"en",
            "TargetLanguageCode":"fr"
        }
    ]    
}
"""

json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping") # This will print to the console as the default level is warning
else:
    logging.info("The SourceLanguageCode and the TargetLanguageCode are different - proceeding") # This will not print to the console because it is lower than warning