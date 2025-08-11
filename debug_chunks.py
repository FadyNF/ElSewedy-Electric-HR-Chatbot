from rag_system import RAGSystem
import os

# Initialize RAG system
rag = RAGSystem()

# Process one document and see chunks
pdf_file = "knowledge_base/Group L&D Policy.pdf"  # Change to any PDF you want
chunks = rag.process_document(pdf_file)

print(f"\n=== CHUNKS FROM {os.path.basename(pdf_file)} ===")
print(f"Total chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, 1):
    print(f"--- CHUNK {i} ({len(chunk)} chars) ---")
    print(chunk)
    print("\n" + "="*50 + "\n")