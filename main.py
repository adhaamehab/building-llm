from src.data import DataLoader

tokens = DataLoader("the-verdict").load()
print(f"Loaded {len(tokens)} characters.")
print(tokens[:99])
