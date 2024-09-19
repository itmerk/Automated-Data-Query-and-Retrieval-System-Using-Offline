from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_mongodb_query(prompt):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(**inputs, max_length=50)
    query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return query

if __name__ == "__main__":
    # Example prompts for test cases
    test_case_1_prompt = "Find all products with a rating below 4.5 that have more than 200 reviews and are offered by the brand 'Nike' or 'Sony'."
    test_case_2_prompt = "Which products in the Electronics category have a rating of 4.5 or higher and are in stock?"
    test_case_3_prompt = "List products launched after January 1, 2022, in the Home & Kitchen or Sports categories with a discount of 10% or more, sorted by price in descending order."

    # Generate queries
    query_1 = generate_mongodb_query(test_case_1_prompt)
    query_2 = generate_mongodb_query(test_case_2_prompt)
    query_3 = generate_mongodb_query(test_case_3_prompt)

    with open('queries_generated.txt', 'w') as f:
        f.write(f"Test Case 1: {query_1}\n")
        f.write(f"Test Case 2: {query_2}\n")
        f.write(f"Test Case 3: {query_3}\n")
