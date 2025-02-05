import os
from dotenv import load_dotenv
load_dotenv()

az_openai_endpoint=os.getenv("az_openai_endpoint")
az_open_ai_key=os.getenv("az_open_ai_key")
az_open_ai_model=os.getenv("az_open_ai_model")
az_deployment_name=os.getenv("az_deployment_name")
az_openai_api_version=os.getenv("az_openai_api_version")
az_openai_coder_assistant_id=os.getenv("az_openai_coder_assistant_id")
az_openai_analyst_assistant_id=os.getenv("az_openai_analyst_assistant_id")
az_data_file_products_master_file_id = os.getenv("az_data_file_products_master_file_id")
az_data_file_products_sales_file_id = os.getenv("az_data_file_products_sales_file_id")
az_openai_vendor_financial_assistant_id = os.getenv("az_openai_vendor_financial_assistant_id")
az_data_file_vendor_financial_statements_file_id = os.getenv("az_data_file_vendor_financial_statements_file_id")
