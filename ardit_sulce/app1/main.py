while True:
    # Get user input and strip space chars from it
    user_action = input('Type add, complete,show or edit: ')
    user_action = user_action.strip()

    # match user_action:
        # Check if user action is 'add'
    if 'add' not in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
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
    if 'edit' in user_action:
        print(number)
        number = user_action[5:]
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        print('Here is todos existing', todos)

        new_todo = input('Enter new todo: ')
        todos[number]= new_todo + '\n'

        print('Here is how it will be', todos)

    if 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        todos.pop(number - 1)

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        message = f'Todo {todo_to_remove} was removed from the list.'

    if 'exit' in user_action:
        break
    else:
        print('Command is not valid')



print('Bye!')