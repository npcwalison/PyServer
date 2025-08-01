from flask import jsonify

def controller_sector(data):
    # Agora a função pode receber os dados do formulário
    nome = data.get('nome')
    descricao = data.get('descricao')

    print(nome)
    print(descricao)

    if not nome:
        raise ValueError("O campo 'nome' é obrigatório")

    return {
        'nome': nome.strip().title(),
        'descricao': descricao.strip() if descricao else None
    }

def controller_users(data):
    # Agora a função pode receber os dados do formulário
    nome = data.get('nome')
    descricao = data.get('descricao')

    print(nome)
    print(descricao)

    if not nome:
        raise ValueError("O campo 'nome' é obrigatório")

    return {
        'nome': nome.strip().title(),
        'descricao': descricao.strip() if descricao else None
    }


def controller_machines(data):
    # Agora a função pode receber os dados do formulário
    nome = data.get('nome')
    descricao = data.get('descricao')

    print(nome)
    print(descricao)

    if not nome:
        raise ValueError("O campo 'nome' é obrigatório")

    return {
        'nome': nome.strip().title(),
        'descricao': descricao.strip() if descricao else None
    }

def controller_events(data):
    # Agora a função pode receber os dados do formulário
    nome = data.get('nome')
    descricao = data.get('descricao')

    print(nome)
    print(descricao)

    if not nome:
        raise ValueError("O campo 'nome' é obrigatório")

    return {
        'nome': nome.strip().title(),
        'descricao': descricao.strip() if descricao else None
    }
