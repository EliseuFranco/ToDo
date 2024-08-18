from . import model
import time

new_task = model.Tarefa()

def linha():
    print('-'*30)

def mensagem(titulo):
    linha()
    print(f'{titulo:^{30}}')
    linha()

def validarEntrada(opcao):
   
    while True:
        try:
            opcao = int(input(opcao))
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Entrada inválida, por favor faça uma entrada válida ex(1,2..)")
            continue
        else:
            return opcao

def menu(tarefas):

    for task in range(len(tarefas)):
        print(f'{task+1} - {tarefas[task]}')

def addTask():
    task_number = validarEntrada("Quantas tarefas quer adicionar: ")

    for i in range(task_number):
        new_task.adicionarTarefa(input(f"Título da {i+1}º tarefa: ").upper(), input(f"Descrição da {i+1}º terefa: ").upper())
    print("Tarefa adicionada com sucesso.")
    time.sleep(1)
    
def viewTask():

    print("Lista de Tarefas:") 
    print(f'{"No":<5} {"Título":<10} {"Descrição":<30}')
    linha()
    if not new_task.visualizarTarefa():
        print("No data to show")
    else:
        for index, data in enumerate(new_task.visualizarTarefa(), start=1):
            for task, desc in data.items():
                print(f'{index:<5} {task.capitalize():<20} {desc.capitalize():<30}')

def verifyTask(titulo):
   return any(titulo in tarefa for tarefa in new_task.excluirTarefa())

def removeTask():

    task = new_task.excluirTarefa()
    if task:
        titulo = input("Título da tatefa: ").upper()
        if verifyTask(titulo):
            if input("Tens certeza que queres eliminar a tarefa[S/N]? ").upper() == 'S':
                for data in range(len(task)):
                    if titulo in task[data].keys():
                        del task[data]
                        break
                print("Tarefa removida com sucesso")
        else:
            print("Tarefa inexiste, informe uma tarefa válida")
    else:
        print("No data do delete")
    
def save(file_name):
    new_task.saveTask(file_name)
    time.sleep(1)

def load(file_name):
    new_task.loadTasks(file_name)


def edit():
    task = new_task.visualizarTarefa()
    if not task:
        print("No data to edit")
    else:
        viewTask()
        linha()
        opc = validarEntrada("Escolha o número da tarefa que seja editar: ")
        if opc > len(task):
            print("índice da tarefa fora do intervalo")
        else:
            new_title = input("Novo titulo: ")
            new_task.editTask(new_title,opc)
            print("Tarefa editada com sucesso")
            time.sleep(1)