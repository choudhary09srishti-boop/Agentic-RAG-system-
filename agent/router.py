from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def classify_intent(query):
    prompt = f"""You are a query classifier. Classify the following query into exactly one of these categories:
- FACTUAL: simple, direct question with a single answer
- COMPLEX: requires combining multiple pieces of information
- OUT_OF_SCOPE: unrelated to the documents

Query: {query}

Reply with only one word: FACTUAL, COMPLEX, or OUT_OF_SCOPE."""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    intent = response.choices[0].message.content.strip().upper()
    if intent not in ["FACTUAL", "COMPLEX", "OUT_OF_SCOPE"]:
        intent = "COMPLEX"
    return intent