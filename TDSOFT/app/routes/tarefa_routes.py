from flask import Flask, jsonify, request
from app.models.tarefa import Tarefa
from app.models.tarefarepository import TarefaRepository
from flasgger import Swagger  # Importando o Swagger

app = Flask(__name__)
Swagger(app)  # Inicializando o Swagger

repository = TarefaRepository()

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    """
    Criar uma nova tarefa
    ---
    parameters:
      - name: tarefa
        in: body
        type: object
        required: true
        properties:
          descricao:
            type: string
            description: Descrição da tarefa
          data_tarefa:
            type: string
            description: Data da tarefa (formato YYYY-MM-DD)
    responses:
      201:
        description: Tarefa criada com sucesso
    """
    dados = request.get_json()
    tarefa = Tarefa(
        descricao=dados['descricao'],
        data_tarefa=dados['data_tarefa']
    )
    repository.criar(tarefa)
    return jsonify(tarefa.__dict__), 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    """
    Listar todas as tarefas
    ---
    responses:
      200:
        description: Lista de tarefas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              descricao:
                type: string
              data_tarefa:
                type: string
    """
    tarefas = repository.listar_todas()
    return jsonify([tarefa.__dict__ for tarefa in tarefas])

@app.route('/tarefas/<tarefa_id>', methods=['GET'])
def buscar_tarefa(tarefa_id):
    """
    Buscar uma tarefa pelo ID
    ---
    parameters:
      - name: tarefa_id
        in: path
        type: string
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Tarefa encontrada
        schema:
          type: object
          properties:
            id:
              type: string
            descricao:
              type: string
            data_tarefa:
              type: string
      404:
        description: Tarefa não encontrada
    """
    tarefa = repository.buscar_por_id(tarefa_id)
    if tarefa:
        return jsonify(tarefa.__dict__)
    return jsonify({"mensagem": "Tarefa não encontrada"}), 404

@app.route('/tarefas/<tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    """
    Atualizar uma tarefa
    ---
    parameters:
      - name: tarefa_id
        in: path
        type: string
        required: true
        description: ID da tarefa
      - name: tarefa
        in: body
        type: object
        required: true
        properties:
          descricao:
            type: string
            description: Nova descrição da tarefa
          data_tarefa:
            type: string
            description: Nova data da tarefa
    responses:
      200:
        description: Tarefa atualizada com sucesso
      404:
        description: Tarefa não encontrada
    """
    dados = request.get_json()
    tarefa = repository.atualizar(tarefa_id, dados['descricao'], dados['data_tarefa'])
    if tarefa:
        return jsonify(tarefa.__dict__)
    return jsonify({"mensagem": "Tarefa não encontrada"}), 404

@app.route('/tarefas/<tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    """
    Deletar uma tarefa
    ---
    parameters:
      - name: tarefa_id
        in: path
        type: string
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    tarefa = repository.deletar(tarefa_id)
    if tarefa:
        return jsonify({"mensagem": "Tarefa deletada com sucesso"})
    return jsonify({"mensagem": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
