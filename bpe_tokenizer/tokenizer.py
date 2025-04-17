from .utils import tokenize_corpus, count_pairs
from collections import defaultdict

class BPETokenizer:
    def __init__(self, vocab_size: int, unk_token="<unk>", pad_token="<pad>"):
        """
        Initialisation du tokenizer avec la taille du vocabulaire désirée.
        """
        self.vocab_size = vocab_size
        self.bpe_codes = {}
        self.unk_token = unk_token
        self.pad_token = pad_token

    def fit(self, corpus: list[str]):
        """
        Entraîne le tokenizer sur un corpus donné.
        Fusionne les paires les plus fréquentes jusqu'à ce que la taille du vocabulaire soit atteinte.
        """

        tokenized_corpus = tokenize_corpus(corpus)

        while len(self.bpe_codes) < self.vocab_size:
            pairs = count_pairs(tokenized_corpus)

            if not pairs:
                print("=====================")
                print("End, not pairs found")
                print("=====================")
                break

            best_pair = max(pairs, key=pairs.get)

            print(f"Fusion de la paire la plus fréquente : {best_pair} avec {pairs[best_pair]} occurrences")

            self._merge_pair(best_pair, tokenized_corpus)

            self.bpe_codes[(self.unk_token,)] = None
            self.bpe_codes[(self.pad_token,)] = None
            self.bpe_codes[best_pair] = len(self.bpe_codes) 
            

    def _merge_pair(self, pair: tuple[str, str], tokenized_corpus: list[list[str]]):
        """
        Fusionne une paire de symboles dans tout le corpus.
        """
        new_token = ''.join(pair)

        for i, sentence in enumerate(tokenized_corpus):
            new_sentence = []
            skip = False
            for j in range(len(sentence)):
                if skip:
                    skip = False
                    continue
                if j < len(sentence) - 1 and (sentence[j], sentence[j+1]) == pair:
                    new_sentence.append(new_token)
                    skip = True
                else:
                    new_sentence.append(sentence[j])
            tokenized_corpus[i] = new_sentence

    def encode(self, text: str) -> list[str]:
        """
        Encode un texte avec les règles de fusion apprises.
        Retourne la liste des tokens finaux.
        """
        from .utils import tokenize_word
        tokens = []

        for word in text.split():
            token = tokenize_word(word)

            while True:
                pairs = [(token[i], token[i + 1]) for i in range(len(token) - 1)]
                pair_to_merge = None

                for pair in pairs:
                    if pair in self.bpe_codes:
                        pair_to_merge = pair
                        break

                if pair_to_merge is None:
                    break

                new_token = []
                i = 0
                while i < len(token):
                    if i < len(token) - 1 and (token[i], token[i + 1]) == pair_to_merge:
                        new_token.append(token[i] + token[i + 1])
                        i += 2
                    else:
                        new_token.append(token[i])
                        i += 1
                token = new_token

            if not all(any(t.startswith(k[0]) for k in self.bpe_codes.keys()) for t in token):
                tokens.append(self.unk_token)
            else:
                tokens.extend(token)

        return tokens
    
    def decode(self, tokens: list[str]) -> str:
        """
        Décode une liste de tokens en texte brut.
        """
        decoded_text = []
        word = []

        for token in tokens:
            if token.endswith('</w>'):
                word.append(token[:-4])
                decoded_text.append(''.join(word))
                word = []
            else:
                word.append(token)
        
        return " ".join(decoded_text)
    
    def save_vocab(self, filename: str):
        """
        Sauvegarde le vocabulaire dans un fichier JSON.
        Les clés de tuple sont converties en chaînes avec un séparateur sûr.
        """
        import json

        bpe_codes_str_keys = {
            "__SEP__".join(key): value for key, value in self.bpe_codes.items()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(bpe_codes_str_keys, f, ensure_ascii=False, indent=2)

    def load_vocab(self, filename: str):
        """
        Charge un vocabulaire depuis un fichier JSON et reconvertit les clés en tuples.
        """
        import json

        with open(filename, 'r', encoding='utf-8') as f:
            bpe_codes_str_keys = json.load(f)

        self.bpe_codes = {
            tuple(key.split("__SEP__")): value for key, value in bpe_codes_str_keys.items()
        }

    def pad_sequences(self, sequences: list[list[str]]) -> list[list[str]]:
        """
        Créé une marge pour completer le manque d'élément.
        """
        max_len = max(len(seq) for seq in sequences)
        padded = []

        for seq in sequences:
            padded_seq = seq + [self.pad_token] * (max_len - len(seq))
            padded.append(padded_seq)

        return padded



    

