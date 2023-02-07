<center>
<img src='https://miro.medium.com/max/1075/0*ZEJgyk4y4vegUsmS.png'>
</center>

O Git Actions é uma ferramenta de automação de tarefas para projetos no GitHub. Com o Git Actions, você pode configurar scripts (conhecidos como "workflows") que serão executados em resposta a eventos específicos, como o push de um novo código ou a abertura de uma issue.

Algumas das funcionalidades do Git Actions incluem:

1. Integração contínua (CI): Você pode configurar workflows para executar testes de unidade, integração e entrega contínua de forma automatizada.

2. Deploy automático: Você pode configurar workflows para implantação automática de seu código em ambientes de produção, teste e desenvolvimento.

3. Geração de documentação: Você pode configurar workflows para gerar e atualizar documentação automaticamente, sem a necessidade de interação manual.

4. Verificação de código: Você pode configurar workflows para verificar o código automaticamente e garantir que atenda a padrões específicos.

5. Integração de terceiros: O Git Actions permite integrar com outras ferramentas e serviços, como o Slack, para melhorar ainda mais a automação de tarefas.

Essas são apenas algumas das muitas funcionalidades do Git Actions. Ao automatizar tarefas, o Git Actions permite que você se concentre no desenvolvimento do seu projeto, aumentando a eficiência e reduzindo a margem de erro humano.

## Exemplo de um arquivo yml para o Git Actions

```yml

name: CI

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ["3.7", "3.8", "3.9", "3.10"]

    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python }}
      - name: Install Tox and any other packages
        run: pip install tox
      - name: Run Tox
        run: tox -e py
```

* `name`: O nome do fluxo de trabalho como aparecerá na guia "Ações" do repositório GitHub

* `on: [push, pull_request]`: Informa ao Actions para executar nossos testes toda vez que enviarmos o código para o repositório ou uma solicitação pull for criada. Se enviarmos alterações de código, nossos testes serão executados. Se alguém criar uma solicitação pull, os testes serão executados. Nas solicitações pull, o resultado da execução do teste pode ser visto na interface da solicitação pull. Todos os resultados da execução da ação podem ser vistos na guia Ações na interface do GitHub. Veremos isso em breve. 

Especifica o gatilho para este fluxo de trabalho. Este exemplo o push, portanto, uma execução de fluxo de trabalho é acionada toda vez que alguém envia uma alteração para o repositório ou mescla uma solicitação pull. Isso é acionado por um push para cada ramificação; para exemplos de sintaxe que são executados apenas em pushes para branches, caminhos ou tags específicos, consulte ["Workflow syntax for GitHub Actions."](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)

* `run-on: ubuntu-latest` especifica em qual sistema operacional executar os testes. Aqui estamos apenas rodando no Linux, mas outros sistemas operacionais estão disponíveis.

Configura o job para ser executado na versão mais recente de um executor do Ubuntu Linux. Isso significa que o trabalho será executado em uma nova máquina virtual hospedada pelo GitHub

* `matrix: python: ["3.7", "3.8", "3.9", "3.10"]`: Especifica qual versão do Python será executada.

* `steps`: É uma lista de etapas. O nome de cada etapa pode ser qualquer um e é opcional.

* `uses: actions/checkout@v2`: é uma ferramenta GitHub Actions que verifica nosso repositório para que o restante do fluxo de trabalho possa acessá-lo.

A palavra-chave `uses` especifica que esta etapa executará `v2` da ação `actions/checkout`. Esta é uma ação que verifica seu repositório no executor, permitindo que você execute scripts ou outras ações em seu código (como ferramentas de compilação e teste). Você deve usar a ação de checkout sempre que seu fluxo de trabalho for executado no código do repositório.

* `uses: actions/setup-python@v2`: É uma ferramenta do GitHub Actions que configura e instala o Python em um ambiente de compilação.

* `with: python-version: ${{ matrix.python }}`: Diz para criar um ambiente para cada
das versões do Python listadas na matriz: python.

* `run: pip install tox`: Instala tox

* `run: tox -e py`: Executa tox. O `-e py` é um pouco surpreendente porque não temos um ambiente `py` especificado. No entanto, isso funciona para selecionar a versão correta do Python especificada em nosso tox.ini.