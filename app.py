import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def read_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)


def summarize_with_openai(prompt):
    try:
        result = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a JSON data analyst that explains and summarizes the content."},
                {"role": "user", "content": prompt}
            ]
        )
        return result.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)


def run_cli():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_content = read_json(file_path)

    preview_data = json.dumps(json_content, indent=2)[:3000]  # Limit size
    summary_prompt = f"Analyze the following JSON and provide a summary:\n{preview_data}"

    print("\n=== AI Summary ===")
    summary = summarize_with_openai(summary_prompt)
    print(summary)

    user_input = input("\nDo you want to ask a question about this data? (y/n): ").strip().lower()
    if user_input == 'y':
        question = input("Enter your question: ")
        question_prompt = f"Based on this JSON:\n{preview_data}\n\nAnswer the following question: {question}"
        print("\n=== AI Answer ===")
        response = summarize_with_openai(question_prompt)
        print(response)


if __name__ == "__main__":
    run_cli()