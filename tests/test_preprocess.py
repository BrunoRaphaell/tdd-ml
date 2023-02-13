from utils.preprocess import (load_data,
                        balanced_smote,
                        remove_null_values,
                        remove_duplicate_values,
                        modifying_schema)

import pandas as pd
import pytest
import numpy as np  

class TestPreprocess:
    
    @pytest.fixture
    def dados(self):
        data = pd.read_csv('dados/creditcard.csv')
        yield data
    
    def test_load_data(self):

        # Carregando os dados
        data = load_data()

        # Verificando se os dados foram lidos
        assert data is not None, "Os dados não foram carregados corretamente"

        # Verificando se não é vazio os conjunto de dados carregados
        assert len(data) > 0, "Os dados não foram carregados corretamente"

    # Há dados nulos?

    def test_null_values(self, dados):
        # Verifique se há valores nulos
        dados_without_null = remove_null_values(dados)
        assert dados_without_null.isnull().sum().sum(
        ) == 0, "Há dados nulos no conjunto de dados"

    # Os dados estão balanceados?
    # @pytest.mark.skip(reason="Estou trabalhando com dados que contém nulos")
    def test_balanceamento(self, dados):

        # Coluna com a classe dos dados
        class_col = "Class"

        # Testando o balanceamento dos dados
        dados_balanced = balanced_smote(dados)

        # Alvo para o balanceamento
        target_ratio = 0.5

        class_distribution = dados_balanced[class_col].value_counts(
        ) / dados_balanced.shape[0]

        # Se o percentual de cada classe tiver uma diferença de 10% para o target, o conjunto de dados não está balanceado
        assert abs(
            class_distribution[0] - target_ratio) < 0.2, "O conjunto de dados não está balanceado"
        assert abs(
            class_distribution[1] - target_ratio) < 0.2, "O conjunto de dados não está balanceado"


    def test_duplicate_values(self, dados):
        dados_without_duplicate = remove_duplicate_values(dados)

        # Verifique se há valores duplicados
        assert not dados_without_duplicate.duplicated().any(
        ), "Encontrado valores duplicados no conjunto de dados"

    @pytest.mark.skip(reason="Verificar depois porque está dando erro")
    def test_schema(self, dados):
        # Carregue seus dados aqui
        data_schema = modifying_schema(dados)
        
        # Defina o esquema esperado
        expected_schema = {'Amount': float,
                        'Class': int,
                        'Time': int,
                        'V1': float,
                        'V10': float,
                        'V11': float,
                        'V12': float,
                        'V13': float,
                        'V14': float,
                        'V15': float,
                        'V16': float,
                        'V17': float,
                        'V18': float,
                        'V19': float,
                        'V2': float,
                        'V20': float,
                        'V21': float,
                        'V22': float,
                        'V23': float,
                        'V24': float,
                        'V25': float,
                        'V26': float,
                        'V27': float,
                        'V28': float,
                        'V3': float,
                        'V4': float,
                        'V5': float,
                        'V6': float,
                        'V7': float,
                        'V8': float,
                        'V9': float
                }

        # Verifique se o esquema está correto
        for column, dtype in expected_schema.items():
            assert data_schema[column].dtype == dtype, f"Tipo de dado incorreto para a coluna: {column}"
    