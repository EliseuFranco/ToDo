import Pacotes.util
import Pacotes.model
import os

file = 'task.json'
Pacotes.util.load(file)

while True:
    Pacotes.util.mensagem("ToDo App")
    Pacotes.util.menu(['Add task', 'View Task', 'Update', 'Remove Task','Edit','Save','Sair'])
    Pacotes.util.linha()
    opc = Pacotes.util.validarEntrada("Escolha uma opção: ")
    
    match opc:
        case 1:
            Pacotes.util.addTask()
        case 2:
            Pacotes.util.viewTask()
        case 3:
            print("In development...")
        case 4:
            Pacotes.util.removeTask()
        case 5:
            Pacotes.util.edit()
        case 6:
            Pacotes.util.save(file)
        case 7:
            break
        case _:
            print("Opção inválida")
    os.system("pause")
    os.system('cls')