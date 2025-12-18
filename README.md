📘 AmbedkarGPT — SemRAG-Based Question Answering System

AmbedkarGPT is a Semantic Retrieval-Augmented Generation (SemRAG) based Question Answering system built over Dr. B. R. Ambedkar’s writings.
The project implements key ideas from the SemRAG research paper, combining semantic chunking, knowledge graphs, and hybrid retrieval to answer questions in a grounded and reliable manner.

This repository was developed as part of the AI Engineering Intern Technical Assignment for Kalpit Pvt. Ltd.

✨ Key Features

Semantic Chunking (SemRAG Algorithm 1)
Text is split into semantically coherent chunks using sentence embeddings and cosine similarity.

Knowledge Graph Construction
Named entities and relations are extracted to build a global semantic graph.

Hybrid Retrieval (SemRAG Core Idea)

Local Search (Equation 4): Vector similarity search over semantic chunks

Global Search (Equation 5): Community-level retrieval using the knowledge graph

LLM-Based Answer Generation
Uses a lightweight local LLM to generate answers strictly grounded in retrieved context.

Hallucination Prevention
A relevance-based confidence gate prevents answering out-of-scope questions.

Live Interactive Demo
An interactive script allows real-time question answering during interviews.

🧠 High-Level Architecture
Ambedkar_book.pdf
        |
Semantic Chunking
        |
Semantic Chunks
        |
Knowledge Graph (Entities + Relations)
        |
Community Detection (Louvain)
        |
Hybrid Retrieval
(Local + Global Search)
        |
Context Selection
        |
Local LLM (Phi-3)
        |
Final Answer

📂 Project Structure
ambedkargpt/
├── data/
│   ├── Ambedkar_book.pdf
│   └── processed/
│       └── chunks.json
│
├── src/
│   ├── chunking/
│   │   ├── buffer_merger.py
│   │   └── semantic_chunker.py
│   │
│   ├── graph/
│   │   ├── entity_extractor.py
│   │   ├── graph_builder.py
│   │   └── community_detector.py
│   │
│   ├── retrieval/
│   │   ├── vector_store.py
│   │   ├── local_search.py
│   │   └── global_search.py
│   │
│   ├── llm/
│   │   └── answer_generator.py
│   │
│   └── pipeline/
│       └── ambedkargpt.py
│
├── demo.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Create a Virtual Environment (Optional)
python -m venv venv

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download Required NLP Resources
python -m nltk.downloader punkt
python -m nltk.downloader punkt_tab
python -m spacy download en_core_web_sm

4️⃣ Install Ollama and Pull Lightweight Model

Install Ollama from: https://ollama.com

ollama pull phi3


Note: Phi-3 was chosen to ensure the system runs smoothly on low-resource machines.

🚀 How to Run
Step 1: Run the Full Pipeline

This performs semantic chunking and knowledge graph construction.

python -m src.pipeline.ambedkargpt


Expected output (approximate):

Semantic Chunking Complete
Total Chunks: ~300
Knowledge Graph Built
Nodes: ~1400
Edges: ~1500

Step 2: Run the Live Demo (Interview-Ready)
python demo.py


Sample questions:

What was Ambedkar’s view on caste?
Why did Ambedkar criticize the Hindu social order?
What is Ambedkar’s idea of social justice?

🛑 Hallucination Handling

If a question is not covered in the source text, the system responds with:

“I cannot answer this question because it is not covered in Dr. B. R. Ambedkar’s writings.”

This behavior is enforced using a relevance gate based on embedding similarity, ensuring safe and grounded answers.

🧠 Approach & Design

This project follows the SemRAG methodology with practical engineering adaptations:

Semantic Chunking
Implements Algorithm 1 from the SemRAG paper using sentence embeddings, buffer merging, and cosine similarity to produce coherent chunks.

Knowledge Graph Construction
spaCy is used to extract entities and simple relations, forming a graph that captures global document structure.

Community Detection
The Louvain algorithm identifies communities of related entities, enabling global semantic reasoning.

Hybrid Retrieval

Local Search retrieves the most relevant chunks using vector similarity (Equation 4).

Global Search leverages entity communities for higher-level context (Equation 5).

Answer Generation with Safety
A lightweight local LLM (Phi-3) generates answers strictly from retrieved context, with a relevance gate to prevent hallucinations.

The system is designed to be modular, explainable, and interview-ready.

📊 Alignment with Assignment Deliverables
✅ Minimum Viable Product

Semantic chunking ✔

Knowledge graph with entities ✔

Local search (Equation 4) ✔

LLM answering questions ✔

Live demo ✔

⭐ Preferred Enhancements

Global search and community detection ✔

Modular and clean codebase ✔

Hallucination prevention ✔

Low-resource local deployment ✔

🔍 Future Improvements

Configurable parameters via config.yaml

Unit tests for individual modules

Graph visualization

Citation-based answers

🧑‍💻 Author

Tanmaya Mathur
AI Engineering Intern Applicant
Kalpit Pvt. Ltd.