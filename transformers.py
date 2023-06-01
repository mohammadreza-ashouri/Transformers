import argparse
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(input_text, model_name='gpt2', max_length=100, num_return_sequences=1):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    inputs = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(inputs, 
                            max_length=max_length, 
                            temperature=0.7, 
                            num_return_sequences=num_return_sequences)

    generated_texts = []
    for token in output:
        generated_texts.append(tokenizer.decode(token, skip_special_tokens=True))

    return generated_texts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_text', type=str, required=True, help='Initial text to generate from')
    parser.add_argument('--model_name', type=str, default='gpt2', help='Model name (default: gpt2)')
    parser.add_argument('--max_length', type=int, default=100, help='Maximum length of the generated text (default: 100)')
    parser.add_argument('--num_return_sequences', type=int, default=1, help='Number of generated sequences (default: 1)')

    args = parser.parse_args()

    generated_texts = generate_text(args.input_text, args.model_name, args.max_length, args.num_return_sequences)
    for i, text in enumerate(generated_texts):
        print(f'Generated Text {i+1}: {text}')

if __name__ == '__main__':
    main()
