from docling.document_converter import DocumentConverter
from docling.chunking import HierarchicalChunker

converter = DocumentConverter()

result = converter.convert("./2408.09869v5.pdf")
document = result.document

chunker = HierarchicalChunker()
chunks = list(chunker.chunk(result.document))

print(chunks[0].text)
