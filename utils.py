"""Helper functions for config and logging."""
import os
from dotenv import load_dotenv
load_dotenv()




def load_config():
return {
'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
'EMBEDDING_MODEL': os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small'),
'COMPLETION_MODEL': os.getenv('COMPLETION_MODEL', 'gpt-4o-mini'),
}
