# SUPER-CSV-ANALYSER-GEMINI-POWERED
⚡ CSV AI Analyst (Gemini Powered)

A fast, schema-aware AI agent that allows you to chat with any CSV file using natural language.

Unlike traditional approaches, this project avoids unnecessary complexity like vector databases and embeddings, and instead focuses on a clean, production-style architecture using LLM + pandas execution.

🚀 Features
📂 Upload any CSV file
💬 Ask questions in natural language
🧠 Automatically understands schema (columns, types, sample data)
⚡ Dynamically generates and executes pandas code
🗣️ Converts results into human-friendly answers
🔒 Structured JSON output for reliable execution
🧠 How It Works
User Query
   ↓
Gemini LLM (Agent)
   ↓
Structured JSON Output
   ↓
If "code" → Execute with pandas
If "text" → Direct response
   ↓
LLM Explanation Layer
   ↓
Final Human-Friendly Answer
💡 Why This Approach?

Most CSV chatbots use:

❌ RAG (Retrieval-Augmented Generation)
❌ Embeddings + Vector DB (FAISS, Pinecone)

This project demonstrates that for structured data:

👉 Pandas + LLM Agent is more efficient than RAG

Benefits:
⚡ Faster response time
🧱 Simpler architecture
🎯 More accurate numerical results
💸 Lower compute cost
🛠️ Tech Stack
Python
Streamlit
Google Gemini API
Pandas
📦 Installation
git clone https://github.com/your-username/csv-ai-analyst.git
cd csv-ai-analyst
pip install -r requirements.txt
🔑 Setup

Add your Gemini API key:

genai.configure(api_key="YOUR_GEMINI_API_KEY")
▶️ Run the App
streamlit run app.py
📊 Example Queries
"What is the average salary?"
"How many people are above age 70?"
"Top 5 highest sales"
"Describe the dataset"
"Which region has the highest revenue?"
💥 Example Output

Query:

How many people are above age 70?

Response:

There are 12 people above the age of 70.

🧠 Key Concepts Implemented
LLM Agent Design
Structured Output (JSON Parsing)
Dynamic Code Generation
Safe Execution Layer
Separation of Computation & Explanation
⚠️ Limitations
Uses eval() for execution (not sandboxed)
Requires clean column naming for best results
No multi-turn memory (yet)
🚀 Future Improvements
📊 Auto chart generation (Plotly)
💬 Conversation memory
🧠 Column synonym understanding
🔐 Secure code execution (sandbox)
🌐 Deployment (public link)
💼 Author

Naghul Maruthasalam
Aspiring AI/ML Engineer | Building practical AI systems

⭐ If you found this useful

Give it a star ⭐ and feel free to connect or contribute!
