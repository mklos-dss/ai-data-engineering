import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as error:
        print(f"Failed to load JSON: {error}")
        sys.exit(1)


def query_openai(message):
    try:
        response = ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data-savvy assistant who interprets JSON files."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as error:
        print(f"OpenAI API error: {error}")
        sys.exit(1)


def run():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = load_json(file_path)

    preview = json.dumps(content, indent=2)[:3000]  # Avoid long prompts
    prompt_intro = f"Below is a JSON dataset:\n{preview}\n\nSummarize the content."

    print("\n--- Summary by AI ---")
    summary = query_openai(prompt_intro)
    print(summary)

    ask = input("\nDo you want to ask a question about this data? (y/n): ").strip().lower()
    if ask == 'y':
        user_question = input("Type your question: ").strip()
        extended_prompt = f"Here is a JSON file:\n{preview}\n\nQuestion: {user_question}"
        print("\n--- AI Response ---")
        response = query_openai(extended_prompt)
        print(response)


if __name__ == "__main__":
    run()
