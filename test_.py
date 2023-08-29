import httpx
import argparse

parser = argparse.ArgumentParser(description='Input doc id.')
parser.add_argument('--id', type=str, help='Input doc id')

args = parser.parse_args()
id = args.id
question = "What is alzheimer's disease?"
external_sources = False

import json

with httpx.stream("GET", f"https://4f98ff2864c224.lhr.life/answer_question/{id}?question={question}&external_sources={external_sources}", timeout=10.0) as response:
    response.raise_for_status()

    for chunk in response.iter_text():
        try:
            data = json.loads(chunk)
            if isinstance(data, dict) and data.get("message") == "streaming finished":
                print("Streaming finished")
                break
        except json.JSONDecodeError:
            data = chunk  # If it's not JSON, treat it as text

        print(data, end='', flush=True)  # Print the response immediately without a newline and flush the output buffer