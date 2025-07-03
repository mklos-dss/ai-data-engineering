# AI Data Analyst DSS – Command Line Tool

This command-line application is built for analysts and data engineers to extract insights from JSON files using OpenAI's GPT models. It streamlines data understanding and question-answering directly from raw structured files.

## Key Features

- Upload JSON files via CLI and get summaries powered by GPT-3.5
- Ask follow-up questions about the data
- Lightweight and dependency-minimal
- Environment-secure with `.env` support for OpenAI API keys

## Installation

```bash
git clone https://github.com/klepacz/ai-data-analyst-dss.git
cd ai-data-analyst-dss
pip install -r requirements.txt
```

## Configuration

Add your OpenAI API key in a `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python app.py path/to/your_file.json
```

You’ll receive a summary and be asked if you want to continue with a specific question.

## Example Output

```
--- AI Summary ---
This dataset contains 500 user session logs. Most sessions lasted under 2 minutes.
40% of users bounced on the homepage.

Ask a follow-up question? (y/n): y
Your question: What’s the bounce rate by device?

--- AI Answer ---
Mobile users had a 52% bounce rate, while desktop was at 33%.
```

## Project Structure

```
├── app.py              # Main CLI tool
├── .env                # Local OpenAI key
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and temp files
```

---

## Tags

openai, json, analytics, cli, gpt, automation, devtools, data-assistant



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