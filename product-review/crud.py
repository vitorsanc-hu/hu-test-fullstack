from models import Produto, Avaliacao
from database import db

def get_produtos():
    return Produto.query.all()

def get_produto(produto_id):
    return Produto.query.get(produto_id)

def create_produto(nome, descricao):
    produto = Produto(nome=nome, descricao=descricao)
    db.session.add(produto)
    db.session.commit()
    return produto

def delete_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False

def create_avaliacao(produto_id, nota, comentario):
    avaliacao = Avaliacao(
        produto_id=produto_id,
        nota=nota,
        comentario=comentario
    )
    db.session.add(avaliacao)
    db.session.commit()
    return avaliacao

def get_avaliacoes():
    return Avaliacao.query.all()

def get_media_produto(produto_id):
    avaliacoes = Avaliacao.query.filter_by(produto_id=produto_id).all()
    if not avaliacoes:
        return None
    
    soma_notas = sum(av.nota for av in avaliacoes)
    media = soma_notas / len(avaliacoes)
    
    return {
        "produto_id": produto_id,
        "media_notas": media,
        "total_avaliacoes": len(avaliacoes)
    } 