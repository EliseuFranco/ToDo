import os
import json
class Tarefa():

    def __init__(self):
        self.tarefas = []
        self.concluido = False

    def adicionarTarefa(self, titulo,descricao=""):

        tasks = {titulo:descricao}
        self.tarefas.append(tasks.copy())

    def visualizarTarefa(self):
        return self.tarefas

    def excluirTarefa(self):
        return self.tarefas

    def saveTask(self, file_name):

        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(self.tarefas, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print("Erro ao salvar as tarefas {e}")
        else:
            print("Tarefa salva com sucesso.")
    
    def loadTasks(self, file_name):
        try:
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    self.tarefas = json.load(f)
            else:
                print(f"Ficheiro {file_name} não encontrado")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
        except Exception as e:
            print(f"Erro ao carregar as tarefas: {e}")
    
    def editTask(self,novo_titulo,opc):

        pos = 0
        old_title = ''

        for i,j in enumerate(self.tarefas):
            for key in j.keys():
                if i == opc:
                    pos = i
                    old_title = key

        aux = {novo_titulo: self.tarefas[pos][old_title]}
        self.tarefas.insert(pos,aux.copy())
        self.tarefas[pos+1].clear()
        self.tarefas.pop(pos+1)


            


