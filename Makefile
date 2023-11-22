# Versão do Python utilizada: 3.10.12

# Comando padrão caso apenas 'make' seja digitado no terminal.
.DEFAULT_GOAL := run

# Nome do arquivo Python que será executado.
PYTHON_FILE := main.py

# Comando para executar o programa Python.
run:
	python3 $(PYTHON_FILE)

# Comando para realizar a limpeza.
clean:
	rm -f symbol_table.csv
