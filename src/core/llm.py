import json
from src.core.bedrock_client import BedrockClient
from src.config.settings import Settings

class LLMClient(BedrockClient):
  def __init__(self, llm_model_id:str, settings: Settings = None, **kwargs):
    # If no settings provided, create a default instance
    self.settings = settings or Settings()
    
    # Prepare kwargs with model ID
    kwargs["BEDROCK_MODEL_ID"] = llm_model_id
    
    # Call parent constructor
    super().__init__(**kwargs)
  
  async def generate_content(self, prompt:str):
    body = {
      "messages": [
        {
          "role": "user", 
          "content": [{"type": "text", "text": prompt}]
        }
      ], 
      **self.settings.get_claude_generation_config()
    }
 
    try:
      response = await self.invoke_model(body)
      
      # Parse the response
      response_body = json.loads(response['body'].read().decode('utf-8'))
      
      # Extract the content from the response
      content = response_body['content'][0]['text']
      return content
    
    except Exception as e:
      print(f"Error in generate_content: {e}")
      raise

