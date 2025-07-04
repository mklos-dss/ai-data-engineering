# AI Data Analyst 004 – JSON CLI Assistant

This command-line tool lets you upload a JSON file and instantly receive structured AI-powered insights. Designed for analysts and developers who want to save time by using OpenAI to quickly understand data.

## Features

- Analyze raw JSON structures via OpenAI’s GPT models
- Interactive Q&A after initial summary
- Minimalistic CLI – no web UI required
- `.env` based API key loading for safety

## Installation

```bash
git clone https://github.com/michalmilosz-ds/ai-data-analyst-004.git
cd ai-data-analyst-004
pip install -r requirements.txt
```

## Configuration

Create a `.env` file with your API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Usage

```bash
python app.py path/to/your_file.json
```

You will get a summary and can optionally ask further questions.

## Sample Output

```
--- AI Summary ---
The dataset contains customer support tickets. Most relate to login issues.
Ticket volume peaked in March.

Ask a follow-up question? (y/n): y
Your question: What login errors were most frequent?

--- AI Answer ---
The majority of login issues were due to incorrect passwords and expired sessions.
```

## Project Layout

```
├── app.py              # CLI script for JSON analysis
├── .env                # Local environment file (excluded from repo)
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to ignore
```

---

## Tags

json, gpt, openai, analytics, ai-assistant, cli, devtools, automation



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