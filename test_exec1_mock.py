from exec1_mock import *
from unittest.mock import Mock 

def test_obter_nome():
    mock_buscar_nome = Mock()
    mock_buscar_nome.return_value = {
        "id": 1,
        "nome": "Gabriel Rafael"
    }
    nome = mock_buscar_nome(1)
    assert nome["nome"] == "Gabriel Rafael"