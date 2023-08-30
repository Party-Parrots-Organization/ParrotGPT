# Basically this file is for fun

Link:
Our application can be found at https://libhackathon-cmx6wwhgfqhhqmcyf4nrfg.streamlit.app/. This is our submission for SMU's Generate Your L(AI)brary Experience 2023 Hackathon.
It is compatible with both desktop and mobile devices.

Purpose:
Our tagline is "The library in your Pocket". Our application is accessible on both desktop and mobile devices.
We want to build an eager AI assistant who cares about your purpose, not just what you're asking for.

Key Features:
- Understands user intent and profile
- Remembers recent interactions
- Backed by reliable data sources (EZprozy and Primo Database, chatlogs)

Tech Stack:
Our entire application has been programmed in python.
The interface is built with the StreamLit UI Library.
We used the LangChain framework to use OpenAI's gpt 3.5-turbo models to interact with external data sources and chat with the user. To allow the model to access SMU Libraries' resources, we used LangChain to instruct the GPT 3.5 model on how to use the Primo API to access the database.
We tokenised chat logs after cleaning the plaintext logs with the Pandas package and stored them as embeddings in a Pinecone database, a vector database.
To interact with external APIs (Primo, EZprozy), we provided documentation to LangChain chains and instructed them to fetch from these APIs.

To better align with user needs, we allowed the model to access historical chat records provided by SMU Libraries.

To ensure that all recommended resources were real and not fabricated by the LLM model, we only allowed the application to recommend resources that were found in SMU Libraries' resource database.
