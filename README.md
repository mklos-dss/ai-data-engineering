# AI Data Engineering – JSON Analysis Assistant

A robust command-line application built to support data engineers in analyzing structured JSON data using OpenAI GPT. It allows automated summaries and insights generation from machine-readable files in a single step.

## Features

- Parse and summarize any JSON document
- Receive GPT-generated analytical commentary
- Ask custom follow-up questions
- Designed for terminal usage with OpenAI API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mklos-dss/ai-data-engineering.git
cd ai-data-engineering
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API Key:
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
```

Make sure to add `.env` to `.gitignore`.

## Usage

Run the app by providing a path to a `.json` file:
```bash
python app.py path/to/your_file.json
```

After the summary, the app will prompt whether you’d like to ask a question.

## Example

```
--- AI Summary ---
This file contains customer orders and shipment statuses for Q2. There is a high delivery failure rate in Region B.

Would you like to ask a follow-up question? (y/n): y
Your question: What caused the delays?

--- AI Answer ---
Most delays were due to logistics partner switchovers and weather issues in the region.
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

## Technologies Used

- Python 3.x
- OpenAI API (gpt-3.5-turbo)
- dotenv for environment management

## Keywords

openai, json, gpt, data-engineering, ai, command-line, analytics



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