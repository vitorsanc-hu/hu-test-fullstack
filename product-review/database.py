from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def populate_sample_data():
    from models import Produto, Avaliacao
    
    if Produto.query.first():
        return
    
    produtos = [
        Produto(nome="Smartphone Galaxy Pro", descricao="Smartphone avançado com câmera de 108MP"),
        Produto(nome="Notebook Dell Inspiron", descricao="Notebook para trabalho e estudos"),
        Produto(nome="Fone Bluetooth Sony", descricao="Fone de ouvido sem fio com cancelamento de ruído"),
        Produto(descricao="Chinelo para caminhada"),
        Produto(nome="Smartwatch Apple", descricao="Relógio inteligente com monitoramento de saúde")
    ]
    
    for produto in produtos:
        db.session.add(produto)
    
    db.session.commit()
    
    avaliacoes = [
        Avaliacao(produto_id=1, nota=5, comentario="Excelente produto! Muito satisfeito."),
        Avaliacao(produto_id=1, nota=4, comentario="Bom smartphone, mas poderia ser mais barato."),
        Avaliacao(produto_id=1, nota=10, comentario="Produto perfeito para o meu uso."),
        
        Avaliacao(produto_id=2, nota=3, comentario="Notebook médio, trava às vezes."),
        Avaliacao(produto_id=2, nota=4, comentario="Bom para o preço."),
        
        Avaliacao(produto_id=3, nota=5, comentario="Som incrível!"),
        Avaliacao(produto_id=3, nota=0, comentario="Odiei o produto"),
        Avaliacao(produto_id=3, nota=-2, comentario="Teste"),

        Avaliacao(produto_id=999, nota=5, comentario="Atendeu as expectativas"),
        
        Avaliacao(produto_id=5, nota=5, comentario="Perfeito para exercícios!"),
        Avaliacao(produto_id=5, nota=4, comentario="Bateria poderia durar mais."),
        Avaliacao(produto_id=5, nota=5, comentario="Recomendo!"),
    ]
    
    for avaliacao in avaliacoes:
        db.session.add(avaliacao)
    
    db.session.commit()
    print("✅ Banco populado com dados de exemplo!")

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        populate_sample_data() 