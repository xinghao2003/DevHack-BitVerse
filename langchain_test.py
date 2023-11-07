# Data Loader for Candidates and Job Description
from langchain.document_loaders.csv_loader import CSVLoader
import openai

loader = CSVLoader(file_path='candidates.csv')
data = loader.load()

#print(data)

openai_organization = "org-IakVZOX3HTBgfcW488pjcEZk"
openai_api_key = "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"

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

db = Chroma.from_documents(data, OpenAIEmbeddings(openai_api_key=openai_api_key, openai_organization=openai_organization))

query = "RPA"
docs = db.similarity_search(query)
print(docs)