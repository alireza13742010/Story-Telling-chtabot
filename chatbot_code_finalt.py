# -*- coding: utf-8 -*-
"""chatbot_code_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JbucY18_HulvFXQUBk4pEP0UWm628nwV
"""

import streamlit as st
import torch
from unsloth import FastLanguageModel

def get_model_response(question):
  attempts = 1  # Number of retry attempts
  max_seq_length = 512
  dtype = None
  load_in_4bit = True
  model, tokenizer = FastLanguageModel.from_pretrained(model_name = "lora_model_story_telling",
  max_seq_length =max_seq_length,dtype = dtype,load_in_4bit = load_in_4bit)
  FastLanguageModel.for_inference(model)
  alpaca_prompt = """Below is an instruction that describes a task, an input that provides question to write and story about it . Write a response that appropriately generate the story based on input with a proper ending.
  ### Input:{}
  ### Response:{}
  """

  for attempt in range(attempts):
    try:
      inputs = tokenizer([alpaca_prompt.format(
      f"{question}",
      "")], return_tensors = "pt").to("cuda")
      outputs = model.generate(**inputs, max_new_tokens = 512, use_cache = True, temperature=0.10, top_k=5,top_p=0.95)
      out_text = tokenizer.batch_decode(outputs,skip_special_tokens=True)
      _ , result= out_text[0].split("Response")
      return result
    except Exception as e:
      if attempt < attempts - 1:
        time.sleep(2)  # Wait for 2 seconds before retrying
      else:
        return f"Error: {str(e)}"
st.title("Story Telling Chatbot")

# Input for the question
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        result = get_model_response(question)
        st.write("Answer:", result)
    else:
        st.write("Please enter a question.")
