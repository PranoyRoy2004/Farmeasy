"""LLM and embedding wrapper functions."""
import os
from dotenv import load_dotenv
load_dotenv()
import openai
from vectorstore import VectorStore
from preprocessing import simple_clean


openai.api_key = os.getenv("OPENAI_API_KEY")


VSTORE_PATH = "faiss_store.bin"


vstore = VectorStore.load(VSTORE_PATH)




def answer_query(question: str, top_k: int = 4) -> str:
"""Return an answer for a user question by retrieving context and calling completion."""
q = simple_clean(question)
docs = vstore.similarity_search(q, k=top_k)
context = "\n\n".join(d['text'] for d in docs)


prompt = f"Use the following context to answer the question. If answer not available, say you don't know.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"


resp = openai.ChatCompletion.create(
model=os.getenv("COMPLETION_MODEL", "gpt-4o-mini"),
messages=[{"role": "user", "content": prompt}],
max_tokens=256,
temperature=0.2,
)
return resp["choices"][0]["message"]["content"].strip()
