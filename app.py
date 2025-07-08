import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not set in .env")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

def call_gpt(data_text, question=None):
    prompt = f"Here is a JSON file:\n\n{data_text}"
    if question:
        prompt += f"\n\nAnswer this question: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional data analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py path/to/file.json")
        sys.exit(1)

    json_path = sys.argv[1]
    data = load_json_file(json_path)
    snippet = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(call_gpt(snippet))

    if input("\nAsk a follow-up question? (y/n): ").lower().strip() == "y":
        q = input("Your question: ")
        print("\n--- AI Answer ---")
        print(call_gpt(snippet, q))

if __name__ == "__main__":
    main()
