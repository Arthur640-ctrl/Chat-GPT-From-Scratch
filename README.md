# Welcome to the Chat-GPT-From-Scratch documentation !

Chat-GPT-From-Scratch is a new IA homemade. The goal is for it to look like Chat GPT, with 0€ and one person to work on this project. This project was made possible by this GitHub [project](https://github.com/ThePixelCrafted/chatgpt_de_zero).

## Table of contents
- [Introduction](#introduction)
- [Features](#features)

## Introduction
Actuellement, il y a ces fonctionnalités :
- [Byte Pair Encoding](./bpe_tokenizer/tokenizer.py)

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
  corpus = ["Hey everyone !"]
  ```
  In the list 'corpus', you need to put the entrainement text. Then you need to train with this line : 
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
  In 'filnale', you need to put the name/path of the file.
  
  *NOTE : When you load a file, you don't need to train the tokenizer*




