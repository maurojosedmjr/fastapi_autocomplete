from app.controllers import controllers


def test_normalize_string():
    ans = controllers.normalize_string("São Paulo")
    assert ans == "sao paulo"
    ans = controllers.normalize_string("Poços De Caldas")
    assert ans == "pocos de caldas"
    ans = controllers.normalize_string("Muzambinho")
    assert ans == "muzambinho"


def test_search_municipio():
    assert len(list(controllers.search_municipio.cache.keys())) == 0
    ans = controllers.search_municipio("pocos")
    assert len(list(controllers.search_municipio.cache.keys())) == 1
    assert len(ans) == 1
    assert ans[0]["nome"] == "Poços de Caldas"
    assert ans[0]["uf_sigla"] == "MG"
    assert len(list(controllers.search_municipio.cache.keys())) == 1
    ans = controllers.search_municipio("muzambinho")
    assert len(ans) == 1
    assert ans[0]["nome"] == "Muzambinho"
    assert ans[0]["uf_sigla"] == "MG"
    assert len(list(controllers.search_municipio.cache.keys())) == 2
