def validate_produto_data(data):
    if not isinstance(data, dict):
        return False, "Dados inválidos"
    
    nome = data.get('nome', '')
    descricao = data.get('descricao', '')
    
    return True, {"nome": nome, "descricao": descricao}

def validate_avaliacao_data(data):
    if not isinstance(data, dict):
        return False, "Dados inválidos"
    
    try:
        nota = int(data.get('nota', 0))
        comentario = data.get('comentario', '')
        
        return True, {"nota": nota, "comentario": comentario}
    except (ValueError, TypeError):
        return False, "Nota deve ser um número"

def produto_to_dict(produto):
    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "avaliacoes": [avaliacao_to_dict(av) for av in produto.avaliacoes]
    }

def avaliacao_to_dict(avaliacao):
    return {
        "id": avaliacao.id,
        "produto_id": avaliacao.produto_id,
        "nota": avaliacao.nota,
        "comentario": avaliacao.comentario
    } 