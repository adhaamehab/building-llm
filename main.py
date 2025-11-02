from src.data import DataLoader
from src.tokenizer import SimpleTokenizerV1, createVocab, preProcessText


raw = DataLoader("the-verdict").load()
print(f"Loaded {len(raw)} characters.")

preprocessed = preProcessText(raw)
print(f"Preprocessed into {len(preprocessed)} tokens.")
print(f"First 20 tokens: {preprocessed[:20]}")

vocab = createVocab(preprocessed)
print(f"Created vocab of size: {len(vocab)}")
print(f"First 20 vocab items: {list(vocab.items())[:20]}")


tokenizer = SimpleTokenizerV1(vocab)

encoded = tokenizer.encode("The desultory life of the Riviera lends itself")
print(f"Encoded: {encoded}")
decoded = tokenizer.decode(encoded)
print(f"Decoded: {decoded}")

assert decoded == "The desultory life of the Riviera lends itself"
