import json
from src.core.bedrock_client import BedrockClient

class LLMClient(BedrockClient):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  
  async def generate_content(self, prompt:str)
