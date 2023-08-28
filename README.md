# AI Chatbot - Generative Response Model

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Future Improvements](#future-improvements)
- [License](#license)

## Introduction

This chatbot utilizes both closed domain and open domain techniques to generate responses based on user input. For open domain responses the chatbot uses a Sequence-to-Sequence (Seq2Seq) architecture to generate responses based on training data from Twitter posts about weather and its replies. For closed domain responses the chatbot uses language modeling techniques such as bag of words, term frequency-inverse document frequency, and word embeddings to match the input to a predetermined response.

## Getting Started

### Prerequisites

- Python 
- TensorFlow
- NLTK
- spaCy('en_core_web_lg')

### Installation

Clone this repository: 
	git clone https://github.com/johnnyyangdiamond/AI-Chatbot.git
	cd AI-Chatbot
	
### Future Improvements

- Use a bigger set of training data so the chatbot replies with more accurate responses
- Write more predetermined responses and a variety of possible entities

### License

This project is licensed under the MIT License


Enjoy experimenting with AI Chatbot. If you have any questions or encounter issues, don't hesitate to reach out to johnnyyangdiamond@gmail.com



	
	



