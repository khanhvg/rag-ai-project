from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", extra="ignore")
  AWS_REGION: str
  BEDROCK_MODEL_ID:str
  POSTGRES_CONNECTION_STRING:str
  MONGODB_CONNECTION_STRING:str
  VECTOR_STORE_TYPE: str="postgres" # or "mongodb"

