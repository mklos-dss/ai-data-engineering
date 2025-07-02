import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)


def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes JSON data."},
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
    data = read_json_file(json_path)

    data_preview = json.dumps(data, indent=2)[:3000]  # Truncate to avoid huge prompts
    base_prompt = f"Here is a JSON dataset:\n{data_preview}\n\nPlease provide a summary of the data."

    print("\n--- AI Summary ---")
    summary = ask_openai(base_prompt)
    print(summary)

    follow_up = input("\nWould you like to ask a question about the data? (y/n): ").strip().lower()
    if follow_up == 'y':
        question = input("Enter your question: ").strip()
        full_prompt = f"Here is a JSON dataset:\n{data_preview}\n\nUser question: {question}"
        print("\n--- AI Answer ---")
        answer = ask_openai(full_prompt)
        print(answer)


if __name__ == "__main__":
    main()