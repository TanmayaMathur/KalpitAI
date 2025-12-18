🚀 AmbedkarGPT
A Semantic RAG (SemRAG) System for Knowledge-Grounded Question Answering

AmbedkarGPT is a Semantic Retrieval-Augmented Generation (SemRAG) based Question Answering system built on Dr. B. R. Ambedkar’s writings.
Unlike traditional RAG pipelines that rely purely on vector similarity, this system integrates semantic chunking, knowledge graphs, and community-aware retrieval to achieve more accurate, structured, and grounded answers.

This project was implemented as part of the AI Engineering Intern Technical Assignment for Kalpit Pvt. Ltd., with a strong focus on research alignment, practical engineering decisions, and interview-ready execution.

🎯 Why This Project Is Different

Most RAG systems:
- Split text arbitrarily
- Retrieve chunks independently
- Hallucinate when context is weak
- AmbedkarGPT solves these issues by design.
- Key differentiators:
✅ Semantic chunking (not fixed-size chunks)
✅ Knowledge graph for global document structure
✅ Hybrid local + global retrieval (as proposed in SemRAG)
✅ Hallucination prevention via relevance gating
✅ Fully local, low-resource execution



🧠 Core Ideas Implemented (From SemRAG Paper)
This project faithfully implements the core concepts of the SemRAG research paper:

SemRAG Concept	                        Implementation
Algorithm 1	        Semantic chunking using embeddings + cosine similarity
Equation (4)	        Local semantic retrieval using FAISS
Equation (5)	        Global retrieval via graph communities
Global Structure	Knowledge graph with Louvain community detection


🏗️ System Architecture (Conceptual Flow)
                Ambedkar_book.pdf
                        ↓
                Semantic Chunking (Algorithm 1)
                        ↓
                Semantic Chunks
                        ↓
                Entity & Relation Extraction
                        ↓
                Knowledge Graph
                        ↓
                Community Detection (Louvain)
                        ↓
                Hybrid Retrieval
                (Local + Global)
                        ↓
                Context Filtering (Relevance Gate)
                        ↓
                Local LLM (Phi-3)
                        ↓
                Final Answer


📂 Repository Structure: 
ambedkargpt/
├── data/
│   ├── Ambedkar_book.pdf
│   └── processed/
│       └── chunks.json
│
├── src/
│   ├── chunking/          # Semantic chunking (SemRAG Algorithm 1)
│   ├── graph/             # Knowledge graph & communities
│   ├── retrieval/         # Local & global retrieval
│   ├── llm/               # Answer generation
│   └── pipeline/          # End-to-end pipeline
│
├── demo.py                # Live interview demo
├── requirements.txt
└── README.md

⚙️ Setup & Installation
1️⃣ Install Python Dependencies
pip install -r requirements.txt

2️⃣ Download NLP Resources
python -m nltk.downloader punkt
python -m nltk.downloader punkt_tab
python -m spacy download en_core_web_sm


3️⃣ Install Ollama & Lightweight LLM
Install Ollama from: https://ollama.com
ollama pull phi3

Why Phi-3?
Chosen deliberately for low memory usage, CPU friendliness, and fast local inference, making the system practical on student laptops.

🚀 Running the System
Step 1 — Build Semantic Chunks & Knowledge Graph
python -m src.pipeline.ambedkargpt

Typical output:
Semantic Chunking Complete
Total Chunks: ~300
Knowledge Graph Built
Nodes: ~1400
Edges: ~1500
Communities: ~400+

Step 2 — Live Question Answering Demo
python demo.py

Try questions like:
What was Ambedkar’s view on caste?
Why did Ambedkar criticize the Hindu social order?
What is Ambedkar’s idea of social justice?


🛑 Hallucination Prevention (Important)

If a question is outside the scope of Ambedkar’s writings, the system refuses to answer:
“I cannot answer this question because it is not covered in Dr. B. R. Ambedkar’s writings.”

How this woEmbedding similarity is used as a relevance confidence gate
- If retrieved context is weak, LLM invocation is skipped
- This makes the system safer and production-oriented

  🧪 What This Project Demonstrates

- Research-to-code translation (SemRAG paper → working system)
- Practical NLP engineering decisions
- Graph-based reasoning beyond vector search
- Responsible LLM usage (hallucination control)
- Clean, modular, extensible design
