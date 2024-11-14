from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, Dict, Any, List

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", extra="ignore")
  
  # AWS Bedrock Configuration
  AWS_REGION: str
  BEDROCK_MODEL_ID:str

  # Database Configuration
  POSTGRES_CONNECTION_STRING:str
  MONGODB_CONNECTION_STRING:str
  VECTOR_STORE_TYPE: str="postgres" # or "mongodb"

  # Claude settings
  CLAUDE_MAX_TOKENS: int = 1000
  CLAUDE_TEMPERATURE: float = 0.2
  CLAUDE_TOP_P: float = 0.9
  CLAUDE_TOP_K: int = 40
  ANTHROPIC_VERSION: str = "bedrock-2023-05-31"

  def get_claude_generation_config(self) -> Dict[str, Any]:
    config = {
      "max_tokens": self.CLAUDE_MAX_TOKENS,
      "temperature": self.CLAUDE_TEMPERATURE,
      "top_p": self.CLAUDE_TOP_P,
      "top_k": self.CLAUDE_TOP_K, 
      "anthropic_version": self.ANTHROPIC_VERSION
    }
    return config