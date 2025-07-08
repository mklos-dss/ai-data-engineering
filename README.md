# AI Data Engine – JSON Analysis CLI

A professional command-line application for analyzing JSON files using OpenAI's GPT models. Designed to support data teams in transforming raw structured data into insights with minimal setup.

## Overview

This tool provides:
- Structured summaries of any valid JSON file
- Option to interactively ask GPT about the data
- Seamless integration with OpenAI API via environment configuration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/miazgamm/ai-data-engine.git
cd ai-data-engine
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Configure your OpenAI API key:
Create a file named `.env` in the project root and add your key:
```env
OPENAI_API_KEY=your_openai_key
```

Ensure `.env` is listed in `.gitignore`.

## Usage

To process a JSON file:
```bash
python app.py path/to/your_file.json
```

The application will return a GPT-based summary. You may then optionally ask a follow-up question.

## Example

```
--- AI Summary ---
The JSON file contains transaction logs for Q4 2023. The largest volume of payments occurred in December, primarily via digital wallets.

Would you like to ask a follow-up question? (y/n): y
Your question: Which customer segment spent the most?

--- AI Answer ---
The enterprise segment had the highest average transaction volume, mainly due to large annual subscriptions.
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

## Technologies

- Python
- OpenAI API
- dotenv
- Terminal-based CLI

## Tags

openai, data-engineering, json, analysis, gpt, cli, automation


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