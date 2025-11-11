"""Simple text cleaning and chunking utilities."""
import re




def simple_clean(text: str) -> str:
text = text.replace('\n', ' ').strip()
text = re.sub(r'\s+', ' ', text)
return text




def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
words = text.split()
chunks = []
i = 0
while i < len(words):
chunk = ' '.join(words[i:i+chunk_size])
chunks.append(simple_clean(chunk))
i += chunk_size - overlap
return chunks
