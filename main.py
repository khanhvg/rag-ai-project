from src.core.embedding import EmbeddingClient
from src.config.settings import Settings
import asyncio



async def main():
  embedding_client = EmbeddingClient(embedding_model_id="cohere.embed-multilingual-v3", settings=Settings())
  texts = ["h", "a"]
  embeddings = await embedding_client.embed_documents(texts)
  print(embeddings)
  
if __name__ == "__main__":
  asyncio.run(main())
