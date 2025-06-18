from flask import Flask, request, jsonify
from flask_cors import CORS
import crud
import schemas
from database import init_db

app = Flask(__name__)
CORS(app, origins=["*"])

init_db(app)

@app.route("/")
def read_root():
    return {"message": "Sistema de Avaliações de Produtos"}

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    try:
        produtos = crud.get_produtos()
        return jsonify([schemas.produto_to_dict(p) for p in produtos])
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/produtos", methods=["POST"])
def criar_produto():
    try:
        data = request.get_json()
        is_valid, result = schemas.validate_produto_data(data)
        
        if not is_valid:
            return jsonify({"error": result}), 400
            
        produto = crud.create_produto(result["nome"], result["descricao"])
        return jsonify(schemas.produto_to_dict(produto)), 201
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/produtos/<int:produto_id>", methods=["GET"])
def obter_produto(produto_id):
    try:
        produto = crud.get_produto(produto_id)
        if produto is None:
            return jsonify({"error": "Produto não encontrado"}), 404
        return jsonify(schemas.produto_to_dict(produto))
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/produtos/<int:produto_id>", methods=["DELETE"])
def deletar_produto(produto_id):
    try:
        sucesso = crud.delete_produto(produto_id)
        if not sucesso:
            return jsonify({"error": "Produto não encontrado"}), 404
        return jsonify({"message": "Produto deletado com sucesso"})
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/produtos/<int:produto_id>/avaliacoes", methods=["POST"])
def criar_avaliacao(produto_id):
    try:
        data = request.get_json()
        is_valid, result = schemas.validate_avaliacao_data(data)
        
        if not is_valid:
            return jsonify({"error": result}), 400
            
        avaliacao = crud.create_avaliacao(produto_id, result["nota"], result["comentario"])
        return jsonify(schemas.avaliacao_to_dict(avaliacao)), 201
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/avaliacoes", methods=["GET"])
def listar_avaliacoes():
    try:
        avaliacoes = crud.get_avaliacoes()
        return jsonify([schemas.avaliacao_to_dict(a) for a in avaliacoes])
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route("/produtos/<int:produto_id>/media", methods=["GET"])
def obter_media_produto(produto_id):
    try:
        media = crud.get_media_produto(produto_id)
        if media is None:
            return jsonify({"error": "Produto não possui avaliações"}), 404
        return jsonify(media)
    except Exception as e:
        return jsonify({"error": "Erro interno"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, use_reloader=True) 