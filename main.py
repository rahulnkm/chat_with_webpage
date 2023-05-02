import streamlit as st
import langchain

from langchain.document_loaders import UnstructuredURLLoader

urls = []


loader = UnstructuredURLLoader(urls=urls)

data = loader.load()
texts = text_splitter.split_text(data)


query = "What did the president say about Justice Breyer"
docs = docsearch.get_relevant_documents(query)


chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
query = "What did the president say about Justice Breyer"
chain.run(input_documents=docs, question=query)