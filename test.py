from bpe_tokenizer.tokenizer import BPETokenizer

corpus = ["bonjour tout le monde"]
tokenizer = BPETokenizer(vocab_size=100)
tokenizer.fit(corpus)

text = "bonjour le monde"
encoded = tokenizer.encode(text)
decoded = tokenizer.decode(encoded)

print("Texte encodé :", encoded)
print("Texte décodé :", decoded)

tokenizer.save_vocab('vocab.json')