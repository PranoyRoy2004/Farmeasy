"""Ingest text files in a folder and build the vector store."""
import argparse
import os
from tqdm import tqdm
from vectorstore import VectorStore
from preprocessing import chunk_text




def ingest(data_dir: str, out_path: str = "faiss_store.bin"):
docs = []
for root, _, files in os.walk(data_dir):
for fname in files:
if not fname.lower().endswith(('.txt', '.md')):
continue
path = os.path.join(root, fname)
with open(path, 'r', encoding='utf-8') as f:
text = f.read()
chunks = chunk_text(text)
for i, c in enumerate(chunks):
docs.append({
'id': f"{fname}-{i}",
'text': c,
'source': path,
})
vs = VectorStore()
print(f"Adding {len(docs)} chunks to vector store...")
vs.add_documents(docs)
vs.save(out_path)
print("Saved vector store to", out_path)




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', required=True)
parser.add_argument('--out', default='faiss_store.bin')
args = parser.parse_args()
ingest(args.data_dir, args.out)
