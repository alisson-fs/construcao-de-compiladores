# Construcao de Compiladores - INE5426

### Alunos: Alisson Fabra da Silva (19200409) e Eduardo Vinicius Betim(19203161)

## Exercução do projeto:

Para exercutar o projeto basta executar o comando abaixo:

make

### Exemplos de código disponíveis;

- factorial.ccc
- matrix.ccc
- sort.ccc

## Alterações feitas na gramática.

### IFSTAT

Modificamos a produção de IFSTAT alterando a chamada do não terminal "STATEMENT" para "{STATELIST}" para tornar a gramática LL1.

### FUNCCALL

Modificamos a produção de FUNCCALL adicionando o terminal "call" no inicio da produção para identificarmos quando o indentificador é de uma função.
