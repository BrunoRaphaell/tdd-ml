import pandas as pd
import json
from imblearn.over_sampling import SMOTE

def load_data():
    data = pd.read_csv('dados/creditcard.csv', nrows=int(284807*0.1))
    return data

def remove_null_values(data):
    return data.dropna()

def balanced_smote(data, target='Class'):
    print(f"Colunas_balanced_smote = {data.columns}")
    X, y = data.drop(target, axis=1), data[target]
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X, y)
    return X_res.join(y_res)

def remove_duplicate_values(data):
    return data.drop_duplicates()

def modifying_schema(data):
    
    schema = """{
                    "Amount": "float",
                    "Class": "int",
                    "Time": "int",
                    "V1": "float",
                    "V10": "float",
                    "V11": "float",
                    "V12": "float",
                    "V13": "float",
                    "V14": "float",
                    "V15": "float",
                    "V16": "float",
                    "V17": "float",
                    "V18": "float",
                    "V19": "float",
                    "V2": "float",
                    "V20": "float",
                    "V21": "float",
                    "V22": "float",
                    "V23": "float",
                    "V24": "float",
                    "V25": "float",
                    "V26": "float",
                    "V27": "float",
                    "V28": "float",
                    "V3": "float",
                    "V4": "float",
                    "V5": "float",
                    "V6": "float",
                    "V7": "float",
                    "V8": "float",
                    "V9": "float"
                }
            """
                        
    # with open("dados/schema_creditcard.json") as f:
    #     schema = json.load(f)
        
    
    for col, dtype in schema.items():
        data[col] = data[col].astype(dtype)
    return data