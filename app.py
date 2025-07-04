import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: Please set your OPENAI_API_KEY in the .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Could not load JSON: {e}")
        sys.exit(1)

def query_openai(data_string, followup=None):
    prompt = f"Analyze this JSON data:\n\n{data_string}"
    if followup:
        prompt += f"\n\nFollow-up question: {followup}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI data analyst."},
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

    path = sys.argv[1]
    data = load_json(path)
    content = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(query_openai(content))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(query_openai(content, question))

if __name__ == "__main__":
    main()
