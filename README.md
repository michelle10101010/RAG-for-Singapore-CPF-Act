# RAG for Singapore CPF Act

A multilingual Retrieval-Augmented Generation (RAG) assistant for the Singapore Central Provident Fund Act 1953.

This project uses Flask for the web interface, Ollama for the local language model, FAISS for vector search, and Nomic multilingual embeddings for document retrieval.

## Disclaimer

This project is for learning and informational purposes only.

It is not legal, financial, tax, CPF planning, or investment advice.

Users should refer to the official Singapore Statutes Online version of the Central Provident Fund Act 1953 and seek professional advice where necessary.

Please avoid entering confidential client information, personal data, or sensitive information into the system.

## Data Source

This project uses the Central Provident Fund Act 1953 from Singapore Statutes Online.

The CPF Act PDF is not included in this repository.

Please download the latest official copy from Singapore Statutes Online:

```text
https://sso.agc.gov.sg/Act/CPFA1953
```

After downloading the PDF, save it inside the `documents/` folder as:

```text
documents/cpf_act.pdf
```

## Features

* Ask questions based on the Singapore Central Provident Fund Act 1953
* Flask-based web interface
* Local RAG system using Ollama
* FAISS vector index for document retrieval
* Multilingual retrieval experiment using `nomic-embed-text-v2-moe`
* FAISS index folder generated locally after the first build
* Chunk size experiment: 2000 characters with 300 overlap
* Curious Bear mascot for a friendly learning interface

## Sample Questions

1. What are the powers of the CPF Board?
2. What does the CPF Act say about CPF contributions by employers?
3. When can CPF money be withdrawn?
4. What happens to CPF money when a member dies?
5. CPF법에 명시된 범죄에는 어떤 것들이 있습니까?
6. Theo Đạo luật CPF của Singapore, người sử dụng lao động phải đóng góp CPF như thế nào?
7. 根据新加坡《中央公积金法令》，雇主需要如何缴交 CPF？

## Project Structure

```text
RAG-for-Singapore-CPF-Act/
├── app.py
├── rag_engine.py
├── test_rag.py
├── requirements.txt
├── README.md
├── .gitignore
├── documents/
├── templates/
└── static/
```

The CPF Act PDF should be placed inside the `documents/` folder as:

```text
documents/cpf_act.pdf
```

After the project is run, the following FAISS index folder will be created automatically:

```text
cpf_act_faiss_nomic_index/
├── index.faiss
└── index.pkl
```

This generated FAISS index folder is not included in the GitHub repository because it can be regenerated locally from the PDF.

## Download the Project

You can download this project from GitHub by clicking:

```text
Code > Download ZIP
```

Then unzip the folder and open it in Terminal, Command Prompt, PowerShell, VS Code Terminal, or Anaconda Prompt.

Alternatively, if you use Git, you may clone the repository:

```bash
git clone <your-repository-url>
cd RAG-for-Singapore-CPF-Act
```

## Requirements

* Python 3.12 recommended
* Ollama installed and running
* Required Python packages listed in `requirements.txt`
* Latest official CPF Act PDF downloaded from Singapore Statutes Online
* CPF Act PDF saved as `documents/cpf_act.pdf`

## Prepare the CPF Act PDF

Download the latest official copy of the Central Provident Fund Act 1953 from Singapore Statutes Online:

```text
https://sso.agc.gov.sg/Act/CPFA1953
```

Save the PDF into the `documents/` folder using this exact filename:

```text
cpf_act.pdf
```

The final file path should be:

```text
documents/cpf_act.pdf
```

The filename is important. If the file is saved using a different name, the app may not be able to find it.

## Ollama Setup

This project uses Ollama to run the local language model and embedding model.

Before running the app, install Ollama from the official Ollama website.

Then pull the required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

You only need to pull these models once on the same computer.

To check whether the models are already installed, run:

```bash
ollama list
```

You should see `llama3.2` and `nomic-embed-text-v2-moe` in the list.

## Apple / macOS Setup

Open Terminal and go into the project folder.

Example:

```bash
cd /path/to/RAG-for-Singapore-CPF-Act
```

### Option A: Using normal Python virtual environment on macOS

Create a virtual environment:

```bash
python3 -m venv rag-env
```

Activate the virtual environment:

```bash
source rag-env/bin/activate
```

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Test the RAG engine:

```bash
python3 test_rag.py
```

Run the Flask app:

```bash
python3 app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

### Option B: Using Anaconda on macOS

Create a conda environment:

```bash
conda create -n cpf-rag python=3.12
```

Activate the conda environment:

```bash
conda activate cpf-rag
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Windows Setup

Windows users may use Command Prompt, PowerShell, VS Code Terminal, or Anaconda Prompt.

If you are new to Python, Anaconda Prompt may be easier because it helps manage Python environments more clearly.

Open your chosen terminal and go into the project folder.

Example:

```bash
cd "C:\path\to\RAG-for-Singapore-CPF-Act"
```

Quotation marks are recommended if the folder path contains spaces.

### Option A: Using normal Python virtual environment on Windows

Create a virtual environment:

```bash
python -m venv rag-env
```

Activate the virtual environment:

```bash
rag-env\Scripts\activate
```

If the above command does not work in Command Prompt, try:

```bash
rag-env\Scripts\activate.bat
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

### Option B: Using Anaconda on Windows

Open Anaconda Prompt and go into the project folder.

Example:

```bash
cd "C:\path\to\RAG-for-Singapore-CPF-Act"
```

Create a conda environment:

```bash
conda create -n cpf-rag python=3.12
```

Activate the conda environment:

```bash
conda activate cpf-rag
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Running the Project Again Later

The environment only needs to be created once.

After the first setup, you do not need to create the environment again.

### If using Anaconda

Open Terminal or Anaconda Prompt, go into the project folder, then run:

```bash
conda activate cpf-rag
python app.py
```

If your macOS setup uses `python3`, run:

```bash
conda activate cpf-rag
python3 app.py
```

### If using normal Python virtual environment on macOS

Open Terminal, go into the project folder, then run:

```bash
source rag-env/bin/activate
python3 app.py
```

### If using normal Python virtual environment on Windows

Open Command Prompt, PowerShell, or VS Code Terminal, go into the project folder, then run:

```bash
rag-env\Scripts\activate
python app.py
```

Then open the local Flask link shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## How the FAISS Index Works

This project uses a FAISS index for document retrieval.

The FAISS index folder is created automatically on first run:

```text
cpf_act_faiss_nomic_index/
```

The folder should contain files such as:

```text
index.faiss
index.pkl
```

This folder is not included in the GitHub repository because it is generated locally.

If this folder is missing, the system should rebuild it from the PDF inside the `documents/` folder.

The first rebuild may take some time.

If the FAISS index folder is deleted, the system should recreate it again on the next run.

## Quick Test Checklist

Before running the app, check the following:

1. The project folder has been downloaded or cloned.
2. The CPF Act PDF has been downloaded from Singapore Statutes Online.
3. The CPF Act PDF is saved as `documents/cpf_act.pdf`.
4. Python environment has been created and activated.
5. Python packages have been installed using `pip install -r requirements.txt`.
6. Ollama is installed and running.
7. The required Ollama models have been downloaded.
8. `python test_rag.py` runs successfully.
9. `python app.py` starts the Flask app successfully.
10. The browser opens `http://127.0.0.1:5000`.

## Troubleshooting

### 1. `pip install -r requirements.txt` does not work

Make sure your Python environment is activated first.

For Anaconda users:

```bash
conda activate cpf-rag
```

For macOS virtual environment users:

```bash
source rag-env/bin/activate
```

For Windows virtual environment users:

```bash
rag-env\Scripts\activate
```

Then try again:

```bash
pip install -r requirements.txt
```

### 2. CPF Act PDF not found

Make sure the CPF Act PDF has been downloaded and saved using the exact file path:

```text
documents/cpf_act.pdf
```

If the file is saved under a different name, rename it to:

```text
cpf_act.pdf
```

### 3. Ollama connection error

Make sure Ollama is installed and running.

You can check whether Ollama is available by running:

```bash
ollama --version
```

You can check installed models by running:

```bash
ollama list
```

If the required models are missing, run:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

### 4. Model not found

Run:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

Then run the app again.

### 5. FAISS index folder is missing

This is expected on a fresh GitHub download.

The app should automatically create the FAISS index folder on first run.

If it does not, run:

```bash
python test_rag.py
```

or on macOS:

```bash
python3 test_rag.py
```

### 6. Port 5000 is already in use

Another Flask app may already be running.

Close the other app, or change the port number inside `app.py`.

For example:

```python
app.run(debug=True, port=5001)
```

Then open:

```text
http://127.0.0.1:5001
```

### 7. The first answer is slow

The first run may take longer because the FAISS index may need to be created from the CPF Act PDF.

After the index is created, future runs should be faster.

### 8. `python` command does not work

On macOS, try:

```bash
python3 --version
```

Then use `python3` instead of `python`.

On Windows, make sure Python has been installed and added to PATH, or use Anaconda Prompt.

### 9. `conda` command does not work

If `conda` is not recognised, Anaconda or Miniconda may not be installed or may not be added to PATH.

You may use the normal Python virtual environment method instead, or open Anaconda Prompt if Anaconda is installed.

## Notes

* This version uses the Nomic multilingual embedding model.
* This version uses FAISS instead of a single pickle index file.
* The CPF Act PDF is not included in this repository.
* Users should download the latest official CPF Act PDF from Singapore Statutes Online.
* The PDF should be saved as `documents/cpf_act.pdf`.
* The FAISS index is saved locally inside the `cpf_act_faiss_nomic_index/` folder after the first build.
* The `cpf_act_faiss_nomic_index/` folder is not included in this repository because it is generated locally.
* The saved FAISS index is built using chunk size 2000 and overlap 300.
* If the FAISS index folder is deleted, the system should rebuild it from the PDF in the `documents/` folder.
* The first rebuild may take some time.
* The assistant answers based on the retrieved Singapore Central Provident Fund Act 1953 document context.
* This project is for learning and experimentation. It is not legal, financial, tax, CPF planning, or investment advice.
* Please avoid entering confidential client information, personal data, or sensitive information into the system.

## Author

Created by Michelle / Curious Bear.

## Special Thanks

* My human teacher, Mr. Go Figure Out, for his encouragement.
* My AI teacher, ChatGPT, for guidance.
