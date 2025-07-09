# AI JSON Tool – Terminal-Based Insight Generator

A terminal-based tool for summarizing and querying structured JSON data using OpenAI's language models. Built to assist analysts and developers in quickly extracting meaning from raw datasets.

## Project Overview

Key capabilities:
- Accepts any valid JSON file as input
- Produces GPT-generated summaries
- Enables follow-up Q&A sessions within the CLI
- API access is securely managed via .env file

## Installation

1. Clone this repository:
```bash
git clone https://github.com/michal-sz-dss/ai_json_tool.git
cd ai_json_tool
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
Create a `.env` file in the root directory with the following content:
```env
OPENAI_API_KEY=your_openai_api_key
```

The `.env` file should be excluded from version control.

## Usage

To analyze a JSON file:
```bash
python app.py path/to/file.json
```

You will receive a structured summary. You may also ask a follow-up question during the session.

## Example

```
--- AI Summary ---
The JSON file contains sales records across three quarters. A spike in revenue occurred in Q2, driven by increased demand in the EU region.

Would you like to ask a follow-up question? (y/n): y
Your question: What was the best-selling category?

--- AI Answer ---
The electronics category led sales, contributing 42% of Q2 revenue.
```

## Project Structure

```
.
├── app.py
├── .env
├── requirements.txt
├── .gitignore
├── README.md
```

## Technologies

- Python 3.x
- OpenAI API
- dotenv
- CLI application design

## Tags

openai, json, data-analysis, python, gpt, cli, automation


## About DS Stream

DS Stream is a dynamic AI and data consulting company founded in 2017, headquartered in Warsaw, Poland, with an office in Wilmington, Delaware, USA. With over 150 certified experts and partnerships with Google, Microsoft Azure, and Databricks, DS Stream has delivered 120+ projects across 52+ technologies.

**Our Expertise**

- 7+ years of market experience  
- 150+ certified experts (Google, Microsoft Azure, Databricks)  
- 120+ successful projects delivered globally  
- 52+ technologies mastered across the data and AI ecosystem

**Core Services**

- **Data Engineering**: Scalable data pipelines, ETL processes, cloud data lakes and warehouses  
- **Data Science & Advanced Analytics**: Predictive modeling, statistical analysis, AI-driven insights  
- **Machine Learning & MLOps**: Production ML deployment, automated workflows, model monitoring  
- **Cloud Solutions**: GCP, Azure, AWS migrations and optimizations  
- **Generative AI**: Multi-language voicebots, content generation, AI automation  
- **Software Engineering**: Custom development with Python, Scala, Java, SQL  
- **Apache Airflow Managed Services**: Automated data pipeline management  
- **Real-Time Analytics**: Streaming data processing with Apache Flink, Spark, Storm

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