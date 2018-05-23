from libpythonpro.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario (nome='joao')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='joao'), Usuario(nome='jones')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
