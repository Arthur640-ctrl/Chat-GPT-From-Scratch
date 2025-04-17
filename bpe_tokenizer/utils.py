from collections import defaultdict

def tokenize_word(word: str) -> list[str]:
    """
    Découpe un mot en caractères avec un marqueur de fin de mot.
    Ex: 'chat' → ['c', 'h', 'a', 't</w>']
    """
    if not word:
        return []
    
    char = list(word)
    char[-1] = char[-1] + "</w>"
    return char

def tokenize_corpus(corpus: list[str]) -> list[list[str]]:
    """
    Tokenize un corpus entier en découpant chaque mot en symboles.
    Ex: ["bonjour tout le monde"] → [['b', 'o', 'n', 'j', 'o', 'u', 'r</w>', 't', 'o', 'u', 't</w>', 'l', 'e</w>', 'm', 'o', 'n', 'd', 'e</w>']]
    """
    tokenized_corpus = []
    
    for sentence in corpus:
        tokenized_sentence = []  
        
        words = sentence.split()
        for word in words:
            tokenized_word = tokenize_word(word)
            tokenized_sentence.extend(tokenized_word)
        
        tokenized_corpus.append(tokenized_sentence)
    
    return tokenized_corpus

def count_pairs(tokenized_corpus: list[list[str]]) -> dict[str, int]:
    """
    Compte la fréquence des paires de symboles dans le corpus.
    Ex: [['b', 'o', 'n', 'j', 'o', 'u', 'r</w>']] → {('b', 'o'): 1, ('o', 'n'): 1, ('n', 'j'): 1, ...}
    """
    pairs = defaultdict(int)
    
    for sentence in tokenized_corpus:
        for i in range(len(sentence) - 1):
            pair = (sentence[i], sentence[i + 1])
            pairs[pair] += 1
    
    return pairs
