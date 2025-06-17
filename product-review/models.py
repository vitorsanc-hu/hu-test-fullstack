from database import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)

    avaliacoes = db.relationship("Avaliacao", back_populates="produto")

class Avaliacao(db.Model):
    __tablename__ = "avaliacoes"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"))
    nota = db.Column(db.Integer)
    comentario = db.Column(db.Text)

    produto = db.relationship("Produto", back_populates="avaliacoes") 