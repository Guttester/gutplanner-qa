# GutPlanner — testes iniciais com Pytest

Projeto simples para verificar se https://planner.guttester.io/ responde via HTTP.

**Dependencia externa unica:** pytest. O acesso HTTP utiliza `urllib.request`, da biblioteca padrao do Python.
Nao utiliza Cypress, Playwright, Selenium, `requests` ou navegador.

## Executar (PowerShell)

Na pasta que contem `pytest.ini`:

```powershell
py -m pip install -r requirements.txt
py -m pytest -v
```

Se seu Windows usa `python` em vez de `py`, substitua `py` por `python`.

## Estrutura

```text
pytest/
├── tests/
│   ├── conftest.py
│   └── test_gutplanner.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## O que testa

- A pagina inicial retorna HTTP 200.
- A resposta tem tipo `text/html` e contem uma tag HTML.

**Limite:** isto nao testa cliques, login ou renderizacao do Angular no navegador. Pytest e o executor dos testes; para automacao visual de navegador, seria necessario integrar outra ferramenta.
