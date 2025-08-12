from rag_system import RAGSystem
import os

# Initialize RAG system
rag = RAGSystem()

# Process one document and see chunks
pdf_file = "knowledge_base/Overseas Travel Policy V03.pdf"  # Change to any PDF you want
document_content = rag.process_document(pdf_file)

print(f"\n=== DOCUMENT CONTENT FROM {os.path.basename(pdf_file)} ===")
print(f"Document length: {len(document_content)} characters\n")
print(f"Word count: {len(document_content.split())} words\n")

print("--- DOCUMENT CONTENT ---")
print(document_content)
print("\n" + "="*50 + "\n")