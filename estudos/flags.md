* `pytest -v -ra`

O sinalizador `-r` diz ao pytest para relatar os motivos de diferentes resultados de teste no final da sessão. Você atribui a ele um único caractere que representa o tipo de resultado sobre o qual deseja obter mais informações

O a in `-ra` significa "todos, exceto aprovados". O sinalizador -ra é, portanto, o mais útil, pois quase sempre queremos saber o motivo pelo qual determinados testes não foram aprovado.

* `pytest -ra --tb=line`

O sinalizador `--tb` controla o tipo de rastreamento de pilha que o pytest exibe quando um teste falha. O valor padrão é `long`, que exibe o rastreamento de pilha completo. O valor `line` exibe apenas a linha onde o erro ocorreu e o valor `no` não exibe nenhum rastreamento de pilha.

* `pytest -ra --tb=line -k "test_1 or test_2"`

O sinalizador `-k` permite que você selecione testes por nome. Você pode usar expressões regulares para selecionar testes. O exemplo acima seleciona os testes `test_1` e `test_2`.

* 