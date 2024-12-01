from uuid import uuid4

class Tarefa:
    def __init__(self, descricao: str, data_tarefa: str):
        self.id = str(uuid4())
        self.descricao = descricao
        self.data_tarefa = data_tarefa
