from unittest.mock import Mock
from libpythonpro.spam.main import EnviadorDeSpam
import pytest

from libpythonpro.spam.models import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [

        [
            Usuario(nome='jones', email='jonescabaltribal@gmail.com'),
            Usuario(nome='joao', email='joaogarciadelimaneto@gmail.com')
        ],

        [
            Usuario(nome='joao', email='joaogarciadelimaneto@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jones', email='jonescabaltribal@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'joaogarciadelimaneto@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

    enviador.enviar.assert_called_once_with == (
        'joaogarciadelimaneto@gmail.com',
        'jonescabaltribal@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
