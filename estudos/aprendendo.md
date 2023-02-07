# TDD para Machine Learning

## Testes de Unidade

Os testes de unidade são a base de seus testes. Eles garantem que uma determinada unidade de nosso produto ou pipeline de ML funcione. Você pode usar o TDD para cada aspecto do pipeline de ML, por exemplo:

* As funções de pré-processamento estão funcionando conforme o esperado?

* Os dados de treinamento estão formatados corretamente?

* Há vazamento de dados, por exemplo, duplicados, no conjunto de dados?

* As métricas são calculadas corretamente?

* O código de treinamento está correto?

* O código de treinamento está funcionando para um problema muito simples?

As funções de pré-processamento comumente construídas em problemas de aprendizado de máquina incluem:

1. Limpeza de dados: remoção de valores ausentes, outliers e duplicatas

2. Conversão de tipo de dados: convertendo dados categóricos em numéricos, por exemplo, usando codificação one-hot

3. Normalização: ajustando a escala dos dados para que todas as características tenham a mesma escala

4. Escalonamento de recursos: ajustar a escala dos dados para que todas as características tenham uma escala similar
5. Divisão de treinamento / teste: separando os dados em conjuntos de treinamento e teste para avaliar o desempenho do modelo

6. Transformações dimensionais: reduzindo a dimensionalidade dos dados usando técnicas como PCA ou t-SNE

Essas são as etapas de pré-processamento mais comuns, mas pode haver outros passos que são aplicados de acordo com as necessidades específicas de cada problema de aprendizado de máquina.

## Testes de Validação

Com os testes de validação, você usa métricas específicas do algoritmo para avaliar como o algoritmo pode ser melhorado. Em aplicações do mundo real, isso geralmente é obtido melhorando a qualidade do conjunto de treinamento. Por exemplo, você pode adicionar mais amostras de casos extremos ou rotular novamente imagens categorizadas incorretamente. Normalmente, esses testes são executados em notebooks Jupyter ou fazem parte de um pipeline de ML automatizado. Nos testes de validação, avalie métricas como:

* Acurácia, precisão, recall, f1_score e AUC.(Para problemas de classificação)

* RMSE, MSE, MAE, R2 (Para problemas de regressão)

* Sobreajuste e subajuste

* Desempenho dentro de cada classe 

* Falsos positivos, falsos negativos, verdadeiros positivos e verdadeiros negativos

## Testes de aptidão

Você deve garantir que seu produto funcione corretamente do ponto de vista do usuário, não apenas do ponto de vista técnico. Os testes de aceitação abrangem todo o produto. Eles devem ser automatizados e baseados no conjunto de teste.

Os testes de aceitação incluem:

* Generalização. O modelo ajusta os dados que não estavam em seu conjunto de teste?

* Métricas específicas do produto (KPIs de negócios).

* Histórias de usuários.

* Correções de bugs.

* Lidando com falhas de ML normalmente.

* End-to-end. Testar a API ou interface. Algo que utilize todos os processos. 


Além de medir o desempenho do algoritmo, você também deve testar o código de treinamento usado para construir o algoritmo. O código incorreto leva a algoritmos ruins que podem fazer com que um modelo tenha um desempenho ruim. Testar corretamente seu pipeline de ML ajuda você a identificar erros mais rapidamente. Responda às seguintes perguntas para ajudar a determinar a causa de seus erros:

Meus resultados são ruins devido a problemas com os dados de treinamento?

Existe simplesmente um erro de codificação?

Minhas métricas são calculadas incorretamente?


## Testando os modelos:

* Desenvolve o modelo no main.py
* Salvar o modelo em pickel
* fazer todos os pré processamentos no test do modelo. Utilizar outro arquivo para fazer o teste do modelo.
* Testar o modelo em outro arquivo como por exemplo a saída esperada.

### Exemplos de testes para testar o modelo de machine learning de classificação

* 