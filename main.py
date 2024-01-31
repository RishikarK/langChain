
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = '7e085a5ca04b534edcb71ecd605d756e7d9ad5249e3a6e58ec375fffb88aeccb'

llm = OpenAI(temperature=0.6)

search = SerpAPIWrapper()
print("Enter The Question : -")
try:
    query = input()
    print("Question:", query)
    response = search.run(query)
    print("Response:", response)
except Exception as e:
    print("Error:", e) #first commit