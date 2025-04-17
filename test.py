from bpe_tokenizer.tokenizer import BPETokenizer

vocab_size = 50  # Taille du vocabulaire
tokenizer = BPETokenizer(vocab_size=vocab_size)

tokenizer.load_vocab('vocab.json')

# Tester la méthode d'encodage
texte = "le chat mange une pomme"
encoded_text = tokenizer.encode(texte)
print(f"Texte encodé : {encoded_text}")

# Tester la méthode de décodage
decoded_text = tokenizer.decode(encoded_text)
print(f"Texte décodé : {decoded_text}")