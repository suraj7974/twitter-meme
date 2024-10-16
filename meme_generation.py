from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


def load_gpt2_model():
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    return model, tokenizer


def generate_meme_text(model, tokenizer, prompt, max_length=50):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1,
                            no_repeat_ngram_size=2, top_k=50, top_p=0.95)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def main():
    model, tokenizer = load_gpt2_model()

    trend = "#MondayMotivation"
    resume_concept = "perfecting your resume"
    prompt = f"Create a meme combining {trend} and {resume_concept}:"

    meme_text = generate_meme_text(model, tokenizer, prompt)
    print(f"Generated meme text: {meme_text}")


if __name__ == "__main__":
    main()
