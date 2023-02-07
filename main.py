import pandas as pd
import pickle
from utils.preprocess import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from utils.model_construction import save_model_pkl


credit_card = load_data()

# Pré-processamento dos dados
credit_card_without_null_values = remove_null_values(credit_card)
credit_card_balanced = balanced_smote(credit_card_without_null_values)
credit_card_without_duplicate = remove_duplicate_values(credit_card_balanced)
credit_card_with_schema = modifying_schema(credit_card_without_duplicate)

# Separando os dados em treino e teste
X = credit_card_with_schema.drop('Class', axis=1)
y = credit_card_with_schema['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Construindo o modelo
rf = RandomForestClassifier(random_state=42, max_depth=10)
rf.fit(X_train, y_train)

# Salvando o modelo serializado
save_model_pkl(rf, "rf_credit_card")

