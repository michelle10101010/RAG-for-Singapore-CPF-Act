from rag_engine import ask_rag

questions = [
    "What does the CPF Act say about CPF contributions by employers?",
    "What are the powers of the CPF Board?",
    "When can CPF money be withdrawn?",
    "What happens to CPF money when a member dies?",
    "What offences are mentioned under the CPF Act?"
]

for question in questions:
    print("=" * 80)
    print("Question:", question)
    print()
    
    answer = ask_rag(question)
    
    print("Answer:")
    print(answer)
    print()
    