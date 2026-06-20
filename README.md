# RAG for Singapore CPF Act

A multilingual Retrieval-Augmented Generation (RAG) assistant for the Singapore Central Provident Fund Act 1953.

This project uses Flask for the web interface, Ollama for the local language model, FAISS for vector search, and Nomic multilingual embeddings for document retrieval.

## Disclaimer

This project is for learning and informational purposes only. It is not legal, financial, tax, CPF planning, or investment advice. Users should refer to the official Singapore Statutes Online version of the Central Provident Fund Act 1953 and seek professional advice where necessary.

## Data Source

This project uses the Central Provident Fund Act 1953 from Singapore Statutes Online.

Please download the latest official copy from:

```text
https://sso.agc.gov.sg/Act/CPFA1953
```

The CPF Act PDF is not included in this repository.

After downloading the PDF, save it in the `documents/` folder as:

```text
documents/cpf_act.pdf
```

## Sample Questions

1. What are the powers of the CPF Board?
2. What does the CPF Act say about CPF contributions by employers?
3. When can CPF money be withdrawn?
4. What happens to CPF money when a member dies?
5. CPF법에 명시된 범죄에는 어떤 것들이 있습니까?
6. Theo Đạo luật CPF của Singapore, người sử dụng lao động phải đóng góp CPF như thế nào?
7. 根据新加坡《中央公积金法令》，雇主需要如何缴交 CPF？

## Features

* Ask questions based on the Singapore Central Provident Fund Act 1953
* Flask-based web interface
* Local RAG system using Ollama
* FAISS vector index for document retrieval
* Multilingual retrieval experiment using `nomic-embed-text-v2-moe`
* FAISS index folder is generated locally after the first build
* Chunk size experiment: 2000 characters with 300 overlap
* Curious Bear mascot for a friendly learning interface

## Project Structure

```text
RAG-for-Singapore-CPF-Act/
├── app.py
├── rag_engine.py
├── test_rag.py
├── requirements.txt
├── README.md
├── documents/
├── templates/
└── static/
```

After the project is run, the following FAISS index folder will be created automatically:

```text
cpf_act_faiss_nomic_index/
```

This generated folder is not included in the GitHub repository.

## Requirements

* Python 3.x
* Ollama installed
* Required Python packages listed in `requirements.txt`
* Latest official CPF Act PDF downloaded from Singapore Statutes Online

## Ollama Models

Pull the required models before running the app:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you are using Python 3 on macOS, you may also use:

```bash
python3 -m pip install -r requirements.txt
```

## Prepare the CPF Act PDF

Download the latest official copy of the Central Provident Fund Act 1953 from Singapore Statutes Online:

```text
https://sso.agc.gov.sg/Act/CPFA1953
```

Save the PDF into the `documents/` folder using this filename:

```text
cpf_act.pdf
```

The final file path should be:

```text
documents/cpf_act.pdf
```

## How to Run

### Step 1: Start Ollama

Open a terminal and run:

```bash
ollama serve
```

If Ollama is already running, you may see a message that the port is already in use. That is fine.

### Step 2: Test the RAG Engine

In the project folder, run:

```bash
python test_rag.py
```

or:

```bash
python3 test_rag.py
```

This checks whether the RAG engine can build or load the FAISS index and answer a test question.

If the `cpf_act_faiss_nomic_index/` folder does not exist yet, the system will build it from the PDF in the `documents/` folder.

### Step 3: Run the Flask App

```bash
python app.py
```

or:

```bash
python3 app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Notes

* This version uses the Nomic multilingual embedding model.
* This version uses FAISS instead of a single pickle index file.
* The CPF Act PDF is not included in this repository.
* Users should download the latest official CPF Act PDF from Singapore Statutes Online.
* The PDF should be saved as `documents/cpf_act.pdf`.
* The FAISS index is saved locally inside the `cpf_act_faiss_nomic_index/` folder after the first build.
* The `cpf_act_faiss_nomic_index/` folder is not included in this repository because it is generated locally.
* The saved FAISS index is built using chunk size 2000 and overlap 300.
* If the FAISS index folder is deleted, the system will rebuild it from the PDF in the `documents/` folder.
* The first rebuild may take some time.
* The assistant answers based on the retrieved Singapore Central Provident Fund Act 1953 document context.
* This project is for learning and experimentation. It is not legal, financial, tax, CPF planning, or investment advice.
* Please avoid entering confidential client information into the system.

## Author

Created by Michelle / Curious Bear

# Special Thanks

My human teacher, Mr. Go Figure Out, for his encouragement.

My AI teacher, ChatGPT, for guidance.
