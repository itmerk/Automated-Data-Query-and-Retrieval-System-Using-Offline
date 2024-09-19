import pandas as pd
import pymongo
from query_generator import generate_mongodb_query

def execute_query(collection, query):
    try:
        query_dict = eval(query)
        result = collection.find(query_dict)
        return list(result)
    except Exception as e:
        print("Error executing query:", e)
        return []

def save_results_to_csv(results, filename):
    if results:
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
    else:
        print("No data found.")

if __name__ == "__main__":
    # Connect to MongoDB
    client=pymongo.MongoClient("mongodb+srv://ramkumarkannan14:oy5lnSKFfmKhooK9@cluster0.pnkpsmo.mongodb.net/")
    db = client["AIQoD"]
    collection = db["Product"]

    # Example prompts for test cases
    test_case_1_prompt = "Find all products with a rating below 4.5 that have more than 200 reviews and are offered by the brand 'Nike' or 'Sony'."
    test_case_2_prompt = "Which products in the Electronics category have a rating of 4.5 or higher and are in stock?"
    test_case_3_prompt = "List products launched after January 1, 2022, in the Home & Kitchen or Sports categories with a discount of 10% or more, sorted by price in descending order."

    # Generate queries
    query_1 = generate_mongodb_query(test_case_1_prompt)
    query_2 = generate_mongodb_query(test_case_2_prompt)
    query_3 = generate_mongodb_query(test_case_3_prompt)

    # Execute test cases and save results
    results_1 = execute_query(collection, query_1)
    save_results_to_csv(results_1, 'test_case_1.csv')

    results_2 = execute_query(collection, query_2)
    save_results_to_csv(results_2, 'test_case_2.csv')

    results_3 = execute_query(collection, query_3)
    save_results_to_csv(results_3, 'test_case_3.csv')
