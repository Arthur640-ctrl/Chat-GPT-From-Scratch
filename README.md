# Welcome to the Chat-GPT-From-Scratch documentation !

Chat-GPT-From-Scratch is a new IA homemade. The goal is for it to look like Chat GPT, with 0€ and one person to work on this project. This project was made possible by this GitHub [project](https://github.com/ThePixelCrafted/chatgpt_de_zero).

## Table of contents
- [Introduction](#introduction)
- [Features](#features)

## Introduction
This project was made possible by this GitHub   [project](https://github.com/ThePixelCrafted/chatgpt_de_zero).

Actually, there are : 
- Tokenizer (BPE : Byte pair Encoding)
Soon :
- CHAT GPT architecture 

## Features
All features :
- [BPETokenizer](#---bpetokenizer---)
- [Features](#features)
  
### -- BPETokenizer --
To use the Tokenizer, you need to define it :
```python
tokenizer = BPETokenizer(vocab_size)
```
Variables :
- 'tokenizer' : You can set the name you want, for call another one function you will use this variable
- 'BPETokenizer' : You should not change this, it is the class of the Tokenizer
- 'vocab_size' : It's the number of token you vocabulary can have

After, you need to set a vocabulary. There are two options :
  - If you start now, you need to create your vacabulary :
  ```python
  corpus = ["Hello everyone, how are you today? Is the world doing well?"]
  ```
  In the list 'corpus', you need to put the entrainement text. Your vocabulary will be established based on what you put in the 'corpus, It is therefore advisable to include a lot of text to establish a large vocabulary. Then you need to train with this line : 
  ```python
  tokenizer.fit(corpus)
  ```
  For save this training, you can add this line :
  ```python
  tokenizer.save_vocab(filename)
  ```
  This line save the vocabulary in a json file. 'Filname' is the name/path of the file.
  - If you already train and save the vocabulary, you can load the vocabulary with this line :
  ```python
  tokenizer.load_vocab(filename)
  ```
  In 'filname', you need to put the name/path of the file.
*NOTE : When you load a file, you don't need to train the tokenizer*
  
After train the Tokenizer or load the vocabulary, you can encode or decode string.

  For encode :
  ```python
  encoded = tokenizer.encode("Hello, word !")
  ```
  *Note : If an élément is not in the vocabulary, there will be <UNK>*

  For decode :
  ```python
  decoded = tokenizer.decode(encoded)
  ```