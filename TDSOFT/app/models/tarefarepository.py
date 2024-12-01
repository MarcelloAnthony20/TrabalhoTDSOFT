from app.models.tarefa import Tarefa
import uuid
from datetime import datetime

class TarefaRepository:
    def __init__(self):
        self.tarefas = []  # Simulação de banco de dados com uma lista

    def criar(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)

    def listar_todas(self):
        return self.tarefas

    def buscar_por_id(self, tarefa_id: str):
        for tarefa in self.tarefas:
            if tarefa.id == tarefa_id:
                return tarefa
        return None

    def atualizar(self, tarefa_id: str, descricao: str, data_tarefa: str):
        tarefa = self.buscar_por_id(tarefa_id)
        if tarefa:
            tarefa.descricao = descricao
            tarefa.data_tarefa = data_tarefa
            return tarefa
        return None

    def deletar(self, tarefa_id: str):
        tarefa = self.buscar_por_id(tarefa_id)
        if tarefa:
            self.tarefas.remove(tarefa)
            return tarefa
        return None
