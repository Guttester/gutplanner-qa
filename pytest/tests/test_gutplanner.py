def test_site_responde_http_200(pagina_gutplanner):
    """Verifica se a URL inicial responde com sucesso."""
    assert pagina_gutplanner["status"] == 200


def test_site_retorna_html(pagina_gutplanner):
    """Confirma que o servidor devolve uma pagina HTML."""
    assert pagina_gutplanner["tipo_conteudo"] == "text/html"
    assert "<html" in pagina_gutplanner["html"].lower()
