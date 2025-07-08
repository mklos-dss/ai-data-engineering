import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is missing from your .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)

def ask_gpt(data_string, question=None):
    prompt = f"Here is a JSON file:\n\n{data_string}"
    if question:
        prompt += f"\n\nAnswer this question based on the file: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data analyst AI assistant."},
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
    data = load_json(path)
    snippet = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(ask_gpt(snippet))

    if input("\nAsk a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Enter your question: ")
        print("\n--- AI Answer ---")
        print(ask_gpt(snippet, question))

if __name__ == "__main__":
    main()
