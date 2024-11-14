import boto3
import json

class BedrockClient:
  def __init__(self, **kwargs):
    self.client = boto3.client(
      service_name="bedrock-runtime",
      region_name=kwargs.get("AWS_REGION")
    )
    self.model_id = kwargs.get("BEDROCK_MODEL_ID")


  async def invoke_model(self, body:dict):
    response = self.client.invoke_model(
      body=json.dumps(body),
      modelId=self.model_id,
      accept="application/json",
      contentType="application/json"
    )
    return response
  
