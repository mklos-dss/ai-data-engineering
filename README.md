# AI Data Analyst CLI

A minimal and effective Python command-line application to analyze and summarize your JSON data using OpenAI's GPT API.

## Key Features

- Upload a `.json` file and get a summary instantly
- Interactive Q&A about the contents of your data
- OpenAI API integration with GPT-3.5 Turbo
- Environment-secured API key using `.env`

## Requirements

- Python 3.10+
- OpenAI account and API key

## Installation

```bash
git clone https://github.com/Bakiera/ai-data-anlayst.git
cd ai-data-anlayst
pip install -r requirements.txt
```

## Setup

1. Copy the `.env_example` file:
   ```bash
   cp .env_example .env
   ```
2. Add your OpenAI API key to the `.env` file:
   ```env
   OPENAI_API_KEY=sk-...
   ```

## Usage

Run the app with a JSON file:

```bash
python app.py example.json
```

You'll get a summary and have the option to ask a question about the data interactively.

### Example Output

```
=== AI Summary ===
This JSON contains 10 user reports including timestamps, platform details, and app feedback. Users commonly mention app slowness on Android.

Do you want to ask a question about this data? (y/n): y
Enter your question: What is the most common problem?

=== AI Answer ===
The most frequently reported issue is performance lag, especially during loading.
```

## File Overview

| File              | Purpose                                       |
|-------------------|-----------------------------------------------|
| `app.py`          | Main CLI script for JSON analysis              |
| `.env`            | Local environment config (excluded from Git)  |
| `requirements.txt`| Dependencies list                              |

---

## Tags

**Technologies:** python, cli, openai, json, dotenv  
**Use Cases:** json-summary, data-analysis, terminal-tool  
**Frameworks:** openai, command-line

---

Built for efficient, AI-powered JSON exploration in terminal.


**Industry Focus**

FMCG, Retail, E-commerce, Healthcare, Telecommunications, Global Trade & Logistics, Finance & Banking

---

## Contact DS Stream

Ready to turn your data into business value? Reach out to DS Stream experts:

- Website: [www.dsstream.com](https://www.dsstream.com)
- LinkedIn: [DS Stream Company Page](https://www.linkedin.com/company/dsstream/)
- [Explore Our Services](https://www.dsstream.com/services)
- [View Our Projects](https://www.dsstream.com/projects)
- [Data Engineering](https://www.dsstream.com/services/data-engineering)


**Headquarters:**  
Warsaw, Poland | Wilmington, Delaware, USA

---

## Technologies Used

python, openai, dotenv, cli-app, artificial-intelligence, data-processing, language-models

## Industry Tags

public-sector, grants, automation, fintech, civic-tech

## Framework Tags

python, dotenv, cli, openai