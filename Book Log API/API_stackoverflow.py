#connect to stack overflow API and return information on questions

import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#print(response)
#print(response.json())
#print(response.json()['items'])

#this loop prints the question title and link of stack over flow questions that have 0 responses, prints "skipped" otherwise
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title']) #prints title of question
        print(data['link']) #prints link to question on stack overflow
        print()
    else:
        print("skipped")
        print()