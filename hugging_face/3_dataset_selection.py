from datasets import load_dataset

# Load the Simple English Wikipedia dump from the Hugging Face Hub
wikipedia = load_dataset("wikimedia/wikipedia", "20231101.simple", split="train")

# Filter the documents
answer = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = answer.select(range(1))

print(example[0]["text"])