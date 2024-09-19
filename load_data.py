# load_data.py
import pandas as pd
import pymongo

def load_csv_to_mongodb(csv_file, db_name, collection_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Connect to MongoDB
    client=pymongo.MongoClient("mongodb+srv://ramkumarkannan14:oy5lnSKFfmKhooK9@cluster0.pnkpsmo.mongodb.net/")
    db = client[db_name]
    collection = db[collection_name]

    # Insert data into MongoDB
    data = df.to_dict('records')
    collection.insert_many(data)
    
    print(f"Data loaded successfully into {db_name}.{collection_name}")

if __name__ == '__main__':
    load_csv_to_mongodb('sample_data.csv', 'AIQoD', 'Product')
