# GPT-2 Simplified Text Generator

Hello everyone, my name is Mo and I'm passionate about all things related to AI and Machine Learning. I've created this project to demonstrate a simplified example of text generation using the GPT-2 model from the `transformers` library by Hugging Face.

## Project Description

The GPT-2 Simplified Text Generator is a Python script that generates text continuations based on a user-provided initial text. It's an interactive and versatile script that provides an introduction to the capabilities of the GPT-2 model for text generation.

## Tech Stack

This project uses the following key technologies:

- **Python**: The script is written in Python.
- **Hugging Face Transformers**: This library provides the pre-trained GPT-2 model and the associated tokenizer.
- **GPT-2 Model**: A state-of-the-art text generation model based on the transformer architecture.

## Usage

The script accepts several command-line arguments, allowing you to customize the input text, the maximum length of the generated text, the model to use (default is 'gpt2'), and the number of text sequences to generate.

Here is a sample usage:

```bash
python transformers.py --input_text "Once upon a time" --model_name gpt2 --max_length 200 --num_return_sequences 3
