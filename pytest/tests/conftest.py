from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pytest


@pytest.fixture(scope="session")
def pagina_gutplanner():
    """Faz um GET real no GutPlanner, sem navegador nem bibliotecas extras."""
    url = "https://planner.guttester.io/"
    requisicao = Request(url, headers={"User-Agent": "GutPlanner-Pytest-Smoke/1.0"})

    try:
        with urlopen(requisicao, timeout=20) as resposta:
            return {
                "url": resposta.geturl(),
                "status": resposta.status,
                "tipo_conteudo": resposta.headers.get_content_type(),
                "html": resposta.read().decode("utf-8", errors="replace"),
            }
    except HTTPError as erro:
        pytest.fail(f"GutPlanner respondeu com HTTP {erro.code}: {erro.reason}")
    except URLError as erro:
        pytest.fail(f"Nao foi possivel acessar {url}: {erro.reason}")
    except TimeoutError:
        pytest.fail(f"Tempo esgotado ao acessar {url}")
