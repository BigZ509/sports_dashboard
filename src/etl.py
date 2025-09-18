import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2
import requests        

# Load environment variables from .env file
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")


#Header for API request
headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

api_url =  "https://nba-api-free-data.p.rapidapi.com/nba-atlantic-team-list"  
# Function to extract data from a public API
def extract_data(api_url):
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame() 

print("API Key:", RAPIDAPI_KEY)
print("API Host:", RAPIDAPI_HOST)
print("API URL:", api_url)

df = extract_data(api_url)
# Function to transform data
#def transform_data(df):
    