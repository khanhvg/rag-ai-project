from src.core.embedding import EmbeddingClient
from src.core.llm import LLMClient
from src.config.settings import Settings
import asyncio



async def main():
  llm_client = LLMClient("anthropic.claude-3-haiku-20240307-v1:0")
  response = await llm_client.generate_content("What is the capital of Vietnam?")
  print(response)  # This will print the actual response text
  # texts = ["h", "a"]
  # embeddings = await embedding_client.embed_documents(texts)
  # print(embeddings)
  
if __name__ == "__main__":
  asyncio.run(main())
