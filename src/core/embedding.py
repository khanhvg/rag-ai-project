import json
from src.core.bedrock_client import BedrockClient

class EmbeddingClient(BedrockClient):
  def __init__(self,embedding_model_id:str, **kwargs):
    kwargs["BEDROCK_MODEL_ID"] = embedding_model_id
    super().__init__(**kwargs)
  
  async def embed_documents(self, texts:list[str], input_type:str="search_document"):

    body = {
      "texts":texts,
      "input_type":input_type
    }

    try:
      response = await self.invoke_model(body)

      # Parse the response
      response_body = json.loads(response.get("body").read().decode("utf-8"))

      # Extract the embeddings from the response
      embeddings = response_body.get("embeddings")
      return embeddings
    except Exception as e:
      print(f"Error embedding documents: {e}")
      return []
