from os import write


def get_todos(filepath):
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    # Get user input and strip space chars from it
    user_action = input('Type add, complete,show or edit: ')
    user_action = user_action.strip()

    # match user_action:
        # Check if user action is 'add'
    if user_action.startswith('add'):
        todo = user_action[4:]

            todos = get_todos('todos.txt')

            todos.append(todo + '\n')

        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

        todos = get_todos()
            # for index, item in enumerate(todos):
            #     print(f'{index}-{item}')
            # print(f'Lenght is {index + 1}')

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
            #print(todos)

            #new_todos =[item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f'{index + 1}-{item}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:0])
            print(number)

            number = number -1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

           write_todos('todos.txt', todos)
        except ValueError:
            print('Your command is not valid.')
            user_action = input('Type add, complete,show or edit: ')
            user_action = user_action.strip()
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number - 1)

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            message = f'Todo {todo_to_remove} was removed from the list.'
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')



print('Bye!')