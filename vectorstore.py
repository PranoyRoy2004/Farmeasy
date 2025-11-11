"""A tiny wrapper around FAISS for storing and retrieving embeddings."""
import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss


EMBED_MODEL = "all-MiniLM-L6-v2"


class VectorStore:
def __init__(self, dim: int = 384):
self.dim = dim
self.model = SentenceTransformer(EMBED_MODEL)
self.index = faiss.IndexFlatL2(dim)
self.metadatas = []


def add_documents(self, docs: list):
texts = [d['text'] for d in docs]
embs = self.model.encode(texts, convert_to_numpy=True)
self.index.add(embs.astype('float32'))
self.metadatas.extend(docs)


def similarity_search(self, query: str, k=4):
q_emb = self.model.encode([query], convert_to_numpy=True).astype('float32')
D, I = self.index.search(q_emb, k)
results = []
for idx in I[0]:
if idx < len(self.metadatas):
results.append(self.metadatas[idx])
return results


def save(self, path: str):
payload = {'metadatas': self.metadatas, 'index': faiss.serialize_index(self.index), 'dim': self.dim}
with open(path, 'wb') as f:
pickle.dump(payload, f)


@classmethod
def load(cls, path: str):
if not os.path.exists(path):
return VectorStore(dim=384)
with open(path, 'rb') as f:
payload = pickle.load(f)
vs = cls(dim=payload.get('dim', 384))
vs.metadatas = payload['metadatas']
vs.index = faiss.deserialize_index(payload['index'])
vs.model = SentenceTransformer(EMBED_MODEL)
return vs
