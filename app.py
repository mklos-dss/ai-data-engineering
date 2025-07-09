import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is missing from .env")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to load JSON: {e}")
        sys.exit(1)

def query_openai(text, question=None):
    prompt = f"This is a JSON file:\n\n{text}"
    if question:
        prompt += f"\n\nNow answer the question: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an experienced data analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py path/to/file.json")
        sys.exit(1)

    path = sys.argv[1]
    json_data = load_json_file(path)
    snippet = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(query_openai(snippet))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(query_openai(snippet, question))

if __name__ == "__main__":
    main()
