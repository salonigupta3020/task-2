from transformers import pipeline

# Load GPT-2 model
gpt2_pipeline = pipeline("text-generation", model="gpt2")

def generate_article_gpt2(prompt):
    generated_text = gpt2_pipeline(prompt, max_length=300, num_return_sequences=1,)
    return generated_text[0]['generated_text']

    if __name__ == "__main__":
        prompt = "The impact of artificial intelligence in healthcare"
        article = generate_article_gpt2(prompt)
        print("GPT-2 Generated Article:\n", article)


    
 
