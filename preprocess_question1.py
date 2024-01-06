import sys
import json
from difflib import SequenceMatcher

def preprocess_text(text):
    return text.lower()

def find_unique_answers(user_question, json_data):
    user_question = preprocess_text(user_question)

    unique_answers = []

    for entry in json_data:
        question = preprocess_text(entry['question'])
        ratio = SequenceMatcher(None, user_question, question).ratio()

        if ratio > 0.6:  # Consider only if similarity > 60%
            for answer in entry['answers']:
                unique_answers.append({
                    'text': answer['text'],
                    'passage': entry['passage']
                })

    return unique_answers

if __name__ == "__main__":
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 preprocess_question1.py <user_question>")
        sys.exit(1)

    user_question = sys.argv[1]

    # Load JSONL data
    with open('data-model-result.jsonl', 'r', encoding='utf-8') as jsonl_file:
        # Read lines and decode each line as a JSON object
        json_data = [json.loads(line) for line in jsonl_file]

    unique_answers = find_unique_answers(user_question, json_data)

    # Print the unique answers as JSON
    if not unique_answers:
        # If no matching answers are found, print an empty JSON response
        print(json.dumps({'results': []}))
    else:
        print(json.dumps({'results': unique_answers}))
