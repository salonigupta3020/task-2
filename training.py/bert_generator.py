from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline

model = AutoModelForMaskedLM.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

#Load BERT model for masked language modeling 
generator = pipeline("fill-mask", model=model, tokenizer=tokenizer)

def generate_article_bert(prompt):
    #simulate article generation by filling in missing parts
    prompt += " [MASK]."
    masked_output  = generator(prompt)
    return masked_output[0]['sequence']


    if __name__ == "__main__":
        prompt = "Artificial intelligence in healthcare has transformed"
        article = generate_article_bert(prompt)
        print("BERT Generated Article:\n", article)
