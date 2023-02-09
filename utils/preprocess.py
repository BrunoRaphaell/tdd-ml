import pandas as pd
import json
from imblearn.over_sampling import SMOTE

def load_data():
    data = pd.read_csv('dados/creditcard.csv')
    return data

def remove_null_values(data):
    return data.dropna()

def balanced_smote(data, target='Class'):
    X, y = data.drop(target, axis=1), data[target]
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X, y)
    return X_res.join(y_res)

def remove_duplicate_values(data):
    return data.drop_duplicates()

def modifying_schema(data):
                            
    with open("dados/schema_creditcard.json") as f:
        schema = json.load(f)
        
    for col, dtype in schema.items():
        data[col] = data[col].astype(dtype)
    return data