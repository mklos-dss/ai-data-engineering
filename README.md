# AI Data Analyst CLI

A command-line tool for analyzing the contents of JSON files using OpenAI's GPT models. Ideal for data analysts, engineers, and scientists who want quick, intelligent summaries and follow-up Q&A powered by generative AI.

---

## 🔍 What It Does

This lightweight Python CLI app allows you to:

- Upload any valid JSON file
- Automatically get a high-level summary using GPT-3.5
- Ask a custom follow-up question about the file content

No dashboards, no UIs — just insights.

---

## ⚙️ How It Works

1. The user provides a path to a local `.json` file.
2. The app sends the JSON content to the OpenAI API.
3. GPT returns a structured summary of what's in the file.
4. Optionally, the user can ask follow-up questions in the terminal.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lukaszmilaszewski-dss/ai-data-analyst-1.git
cd ai-data-analyst-1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API key

Create a file called `.env`:

```env
OPENAI_API_KEY=your_openai_key_here
```

Make sure `.env` is excluded in `.gitignore`.

---

## 🧪 Usage

```bash
python app.py path/to/data.json
```

You will see an AI-generated summary of the file content. You’ll then be asked whether you want to ask a follow-up question interactively.

---

## 💡 Example

```
--- AI Summary ---
The file contains metadata and performance statistics for five marketing campaigns. The third campaign underperformed significantly.

Would you like to ask a follow-up question? (y/n): y
Your question: Why did campaign 3 fail?

--- AI Answer ---
Campaign 3 suffered from low CTR and was targeted to an audience outside the desired segment.
```

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── .env               # Your local OpenAI key (excluded from repo)
├── .gitignore
├── README.md
```

---

## 🧠 Built With

- Python
- OpenAI API
- Python-dotenv
- Terminal / CLI

---

## 🏷️ Tags

openai, data-analysis, json, cli-tool, automation, gpt, insights




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