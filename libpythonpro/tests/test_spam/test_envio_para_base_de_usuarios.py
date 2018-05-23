from libpythonpro.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtde_email_enviados
