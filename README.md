# Basically this file is for fun

Link:
Our application can be found at https://libhackathon-cmx6wwhgfqhhqmcyf4nrfg.streamlit.app/. This is our submission for SMU's Generate Your L(AI)brary Experience 2023 Hackathon.
It is compatible with both desktop and mobile devices.

Purpose:
Our tagline is "Not just the what, but the why".
We want to build an eager AI assistant who cares about your purpose, not just what you're asking for.

Key Features:
- Understands user intent and profile
- Remembers recent interactions
- Backed by reliable data sources (EZprozy and Primo Database, chatlogs)

Tech Stack:
Our entire application has been programmed in python.
The interface is built with the StreamLit UI Library.
We used the LangChain framework to use OpenAI's gpt 3.5-turbo models to interact with external data sources and chat with the user.
We tokenised chat logs and stored them as embeddings in a Pinecone database, which is a vector database.
To interact with external APIs (Primo, EZprozy), we provided documentation to LangChain chains and instructed them to fetch from these APIs.

Miscellaneous Files
The scripts used to clean the datasets and configure the Pinecone database can be found here: