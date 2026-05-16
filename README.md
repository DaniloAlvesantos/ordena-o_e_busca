# 🚀 Passo a passo para rodar o projeto Flask

Este guia explica como configurar e executar o projeto localmente.

---

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

## 2. Criar e ativar o ambiente virtual (.venv)

Windows
```
python -m venv .venv
.\.venv\Scripts\activate
```

Linux / MacOS
```
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar dependências
pip install flask

```
pip install -r requirements.txt
```

4. Inicializar banco de dados (SQLite)

Se existir script de inicialização:
```
python init_db.py
```
Ou garanta que o arquivo:
```
database.db
```

exista no projeto.

6. Rodar o servidor Flask
```
flask run --debug
```