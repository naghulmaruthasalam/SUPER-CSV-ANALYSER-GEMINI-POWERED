import streamlit as st
import pandas as pd
import google.generativeai as genai
import json

# ------------------ CONFIG ------------------
genai.configure(api_key="your key")
model_llm = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="CSV AI Analyst", layout="wide")

# ------------------ HELPERS ------------------

def create_schema(df):
    return {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "sample": df.head(3).to_dict()
    }

def ask_gemini(prompt):
    try:
        response = model_llm.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"

def parse_response(response):
    try:
        return json.loads(response)
    except:
        return {"type": "text", "content": response}

# ------------------ AGENT ------------------

def agent(schema, query):
    prompt = f"""
You are a data analyst.

Return STRICT JSON only.

Format:
{{
  "type": "code" OR "text",
  "content": "your answer"
}}

Rules:
- If calculation needed → type = "code"
- Code must be valid pandas using df
- If explanation → type = "text"
- No markdown
- No extra text
- No incomplete code

Example:
{{
  "type": "code",
  "content": "df['salary'].mean()"
}}

Schema:
{schema}

Query:
{query}
"""
    return ask_gemini(prompt)

# ------------------ UI ------------------

st.title("CSV AI Analyst (Gemini Powered)")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    schema = create_schema(df)

    query = st.text_input("Ask your question")

    if query:
        with st.spinner("Thinking..."):

            raw = agent(schema, query)
            parsed = parse_response(raw)

            try:
                # ---------------- CODE EXECUTION ----------------
                if parsed["type"] == "code":
                    code = parsed["content"]

                    result = eval(code, {}, {"df": df})

                   
                    explanation = ask_gemini(f"""
User Question: {query}
Result: {result}

Give a short, clear, human-friendly answer in one sentence.
Do not mention code.
""")

                    st.subheader("Answer")
                    st.write(explanation)

                    # Optional debug
                    with st.expander("Details"):
                        st.write("Code:", code)
                        st.write("Result:", result)

                # ---------------- TEXT RESPONSE ----------------
                else:
                    st.subheader("Answer")
                    st.write(parsed["content"])

            except Exception as e:
                st.subheader("Answer")
                st.write(parsed.get("content", raw))
                st.warning(f"Execution fallback: {e}")