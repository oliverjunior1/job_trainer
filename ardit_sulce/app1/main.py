while True:
    # Get user input and strip space chars from it
    user_action = input('Type add, complete,show or edit: ')
    user_action = user_action.strip()

    match user_action:
        # Check if user action is 'add'
        case 'add':
            todo = input('Enter a todo:')+'\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
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
        case 'edit':
            number = int(input('Number of the todo to edit:'))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number]= new_todo
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)
        case 'exit':
            break


print('Bye!')