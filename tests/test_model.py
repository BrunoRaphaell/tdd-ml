import pandas as pd 
import pytest
from sklearn.metrics import accuracy_score

from utils.model_construction import load_artefacts
from utils.preprocess import (load_data,
                        balanced_smote,
                        remove_null_values,
                        remove_duplicate_values,
                        modifying_schema)

dados = load_data()
credit_card_without_null_values = remove_null_values(dados)
credit_card_balanced = balanced_smote(credit_card_without_null_values)
credit_card_without_duplicate = remove_duplicate_values(credit_card_balanced)
dados_final = modifying_schema(credit_card_without_duplicate)

class TestModel:
    
    # Testar se o modelo está sendo salvo
    def test_save_model(self):
        pass
    
    def test_model(self):
        # Arrange
        model = load_artefacts("rf_credit_card")
        assert model is not None, "O modelo não foi carregado corretamente"
    
        # Verificar se o modelo possui as propriedades esperadas
        assert hasattr(model, "predict"), "O modelo não possui a função 'predict'"
        assert hasattr(model, "fit"), "O modelo não possui a função 'fit'"
        
    def test_acceptance(self):
        model = load_artefacts("rf_credit_card")
        X = dados_final.drop('Class', axis=1)
        y = dados_final['Class']
        y_pred = model.predict(X)
        assert accuracy_score(y, y_pred) > 0.95, "A acurácia do modelo não está satisfatória"
        
    # Não está sendo testado o código feito para as predições
    def test_prediction(self):
        model = load_artefacts("rf_credit_card")
        
        amostra = [ 4.06000000e+02, -2.31222654e+00,  1.95199201e+00, -1.60985073e+00,
        3.99790559e+00, -5.22187865e-01, -1.42654532e+00, -2.53738731e+00,
        1.39165725e+00, -2.77008928e+00, -2.77227214e+00,  3.20203321e+00,
       -2.89990739e+00, -5.95221881e-01, -4.28925378e+00,  3.89724120e-01,
       -1.14074718e+00, -2.83005567e+00, -1.68224682e-02,  4.16955705e-01,
        1.26910559e-01,  5.17232371e-01, -3.50493686e-02, -4.65211076e-01,
        3.20198199e-01,  4.45191675e-02,  1.77839798e-01,  2.61145003e-01,
       -1.43275875e-01,  0.00000000e+00]
        
        assert model.predict([amostra]) == 1, "A predição não está correta"

    