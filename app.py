import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: Missing OPENAI_API_KEY in .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def parse_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as err:
        print(f"Failed to open file: {err}")
        sys.exit(1)

def call_openai(data_string, user_question=None):
    prompt = f"Analyze the following JSON data:\n\n{data_string}"
    if user_question:
        prompt += f"\n\nFollow-up question: {user_question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for data analysis."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    json_obj = parse_json(json_path)
    formatted_json = json.dumps(json_obj, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(call_openai(formatted_json))

    follow = input("\nAsk a follow-up question? (y/n): ").strip().lower()
    if follow == "y":
        q = input("Enter your question: ")
        print("\n--- AI Answer ---")
        print(call_openai(formatted_json, q))

if __name__ == "__main__":
    main()
