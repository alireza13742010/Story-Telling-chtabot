# Story-Telling-chtabot

# Chatbot with Fine-Tuning using Excel Dataset

## Overview

This repository contains code for a conversational AI chatbot developed through fine-tuning a pre-trained language model. The chatbot is trained on a customized dataset, which is conveniently formatted and stored in an Excel file. The goal of this project is to demonstrate how to adapt a powerful language model to respond intelligently and contextually to user inputs.

## Features

- **Custom Training**: Fine-tuned on a specific dataset to improve relevance and engagement in conversations.
- **Excel Dataset**: Utilizes an Excel file as input data, making it easy to edit and manage conversational pairs.
- **Interactive**: Engages users in a natural language conversation, providing relevant and context-aware responses.
- **Extensible**: Users can easily add more training data to improve the chatbot's knowledge and capabilities.

## Technologies Used

- Python
- Hugging Face Transformers
- Pandas
- OpenAI GPT-3/GPT-4 or similar Language Model
- Jupyter Notebook / Python Scripts

## Getting Started

### Prerequisites

- Python 3.12
- Access to an appropriate model from Hugging Face or OpenAI (or any other pretrained model)


### Fine-tuning the Chatbot

1. Once the fine-tuning process is complete, you can test your chatbot by running:
   ```bash
   python chatbot_code_finalt.py
   ```

### Sample Usage

```python
# Example interaction
question = st.text_input("Enter your question:")
result = get_model_response(question)
print(result)  # Outputs a response based on fine-tuning
```

## Results 
![Story_telling_chatbot](https://github.com/user-attachments/assets/e848e12c-ff1d-4e5a-89be-f235b8dc99e9)

