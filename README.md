# AI Data Analyst – CLI Tool

A command-line tool designed for processing and analyzing JSON data files using OpenAI's GPT models. This application enables structured insights extraction and interactive follow-up queries directly from the terminal.

## Overview

This tool enables users to:
- Upload and parse structured JSON files
- Automatically summarize contents with GPT-3.5
- Ask detailed follow-up questions about the data
- Manage OpenAI credentials via `.env` file

## Installation

1. Clone the repository:
```bash
git clone https://github.com/arturroszko/ai-data-analyst.git
cd ai-data-analyst
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_key
```

Ensure `.env` is excluded from the repository using `.gitignore`.

## Usage

```bash
python app.py path/to/file.json
```

After the summary, the CLI allows you to ask follow-up questions about the content.

## Example

```
--- AI Summary ---
The JSON contains invoice records for Q1 2024. The highest revenue was recorded in March, driven by SaaS product sales.

Would you like to ask a follow-up question? (y/n): y
Your question: What customer segment contributed most?

--- AI Answer ---
The SMB segment accounted for 58% of total Q1 revenue, with notable growth in subscription renewals.
```

## Project Structure

```
.
├── app.py
├── .env               # (excluded)
├── .gitignore
├── requirements.txt
├── README.md
```

## Technologies Used

- Python
- OpenAI API
- python-dotenv
- CLI interface

## Tags

openai, gpt, data-analysis, json, automation, analytics, insights


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