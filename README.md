# AI Data Engineer – JSON CLI Assistant

A streamlined command-line tool that enables AI-powered analysis of JSON files. Ideal for data engineers and analysts who want quick answers and summaries from raw data using OpenAI.

## Features

- Accepts JSON files as input
- Provides structured summaries and insights using GPT-3.5
- Interactive follow-up questions supported
- Minimal setup, runs directly in terminal

## Installation

```bash
git clone https://github.com/michal-rudawski/ai-data-engineer.git
cd ai-data-engineer
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

```bash
python app.py path/to/input.json
```

Get an immediate summary and optionally ask custom questions about the data.

## Sample Output

```
--- AI Summary ---
The JSON includes IoT telemetry data from 5 devices. Common anomalies include voltage spikes and missing temperature values.

Ask a follow-up question? (y/n): y
Your question: Which devices had the most voltage spikes?

--- AI Answer ---
Device ID 103 and 205 had the highest number of voltage anomalies.
```

## Repository Contents

```
├── app.py              # CLI interface for analysis
├── .env                # Local environment variable file
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore .env and caches
```

---

## Tags

openai, json, data-engineering, gpt, analytics, automation, terminal, cli


**Industry Focus**

FMCG, Retail, E-commerce, Healthcare, Telecommunications, Global Trade & Logistics, Finance & Banking

---

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