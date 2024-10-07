from transformers import pipeline

#Load T5 model for text generation 
t5_pipeline = pipeline("text2text-generation", model="t5-small")

def generate_article_t5(prompt):
    t5_input = "generate article: " + prompt
    t5_output = t5_pipeline(t5_input, max_length=300)
    return t5_output[0]['generated_text']

    if __name__ == "__main":
        prompt = "The future of AI healthcare will revolutionize"
        article = generate_article_t5(prompt)
        print("T5 Generated Article:\n", article)