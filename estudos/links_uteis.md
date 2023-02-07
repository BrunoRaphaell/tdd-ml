# Links:

https://www.ibm.com/garage/method/practices/reason/tdd-and-machine-learning/
https://www.oreilly.com/library/view/thoughtful-machine-learning/9781449374075/ch01.html
https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_4_PerformanceMetrics/ThresholdBased.html
https://github.com/opeyemibami/TDD-in-MLOps
https://github.com/wimlds/berlin-tdd-workshop

**Configurando o coverage**
https://pytest-cov.readthedocs.io/en/latest/config.html

**Entenendo o Git Actions**
https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

**Diferença entre pip install e `python -m pip install`**
https://stackoverflow.com/questions/25749621/whats-the-difference-between-pip-install-and-python-m-pip-install

`pip install` e `python -m pip install` são dois comandos que servem para instalar pacotes ou bibliotecas em Python. A principal diferença entre eles está no modo como o Python interpreta o comando.

A flag -m é utilizada para informar ao interpretador Python que o comando a ser executado é um módulo Python. Quando utilizamos `python -m pip install`, o interpretador Python procura o arquivo pip como se fosse um módulo Python e o executa.

Já ao utilizar apenas pip install, o sistema operacional tenta localizar o executável pip na lista de caminhos de busca de comandos (como o PATH). Se o executável pip não estiver presente nessa lista, o sistema operacional não será capaz de encontrá-lo e o comando resultará em erro.

Em resumo, a flag -m é usada para garantir que o interpretador Python execute o comando como se fosse um módulo, enquanto a falta dela significa que o sistema operacional tentará localizar o executável pip como se fosse um comando de linha de comando.