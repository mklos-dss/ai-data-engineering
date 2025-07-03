import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Initialize client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as err:
        print(f"Error reading JSON file: {err}")
        sys.exit(1)

def analyze_with_ai(content, question=None):
    base = f"You are a data expert. Analyze this JSON:\n\n{content}"
    if question:
        base += f"\n\nUser question: {question}"

    try:
        result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful data assistant."},
                {"role": "user", "content": base}
            ]
        )
        return result.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file>")
        sys.exit(1)

    path = sys.argv[1]
    json_data = parse_json(path)
    json_preview = json.dumps(json_data, indent=2)[:3500]

    print("\n--- Summary ---")
    print(analyze_with_ai(json_preview))

    follow_up = input("\nAsk a question about this data? (y/n): ").lower()
    if follow_up == "y":
        q = input("Enter your question: ")
        print("\n--- Answer ---")
        print(analyze_with_ai(json_preview, q))

if __name__ == "__main__":
    main()
