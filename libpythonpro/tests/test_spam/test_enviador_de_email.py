import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'joaogarciadelimaneto@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'joaogarciadelimaneto@gmail.com',
        'Cursos',
        'Turma'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'joao']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'joaogarciadelimaneto@gmail.com',
            'Cursos',
            'Turma'
            )
