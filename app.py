import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Failed to read JSON file: {e}")
        sys.exit(1)

def ask_ai(prompt_text):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data analyst AI. Provide useful summaries and insights from structured JSON data."},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[!] OpenAI API Error: {e}")
        sys.exit(1)

def run():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    data = read_json(file_path)
    snippet = json.dumps(data, indent=2)[:3500]

    base_prompt = f"Here is a JSON dataset:\n\n{snippet}\n\nPlease summarize the key insights."
    print("\n[AI Summary]")
    print(ask_ai(base_prompt))

    follow_up = input("\nWould you like to ask a custom question about the data? (y/n): ").strip().lower()
    if follow_up == "y":
        question = input("Your question: ")
        custom_prompt = f"Given this JSON data:\n\n{snippet}\n\nAnswer this question: {question}"
        print("\n[AI Answer]")
        print(ask_ai(custom_prompt))

if __name__ == "__main__":
    run()
