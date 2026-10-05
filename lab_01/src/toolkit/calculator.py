
operator_priorities = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}



def is_number(token: str) -> bool: # проверяем число ли токен или нет
    try:
        float(token)
        return True
    except ValueError:
        return False

def to_reverse_polish_notation(user_input: str) -> list:
    tokens = user_input.split()
    stack = []
    output = []

    for token in tokens:
        
        # если токен число сразу в итоговый результат
        if is_number(token):
            output.append(token)
        
        # если скобка помешаем ее в стек
        elif token == '(':
            stack.append(token)
            
        # выкидываем все из стека до открытой скобки чтобы реализовать приорит ()
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        
        # если токен - оператор сравниваем его приоритет с операторами в стеке до того момента пока в стеке лежит оператор с приоритетом выше или таким-же как у нового 
        # и выталкиваем такие операторы из стека потом добовляем текущий оператор в стек

        elif token in operator_priorities:
            current_operator_priority = operator_priorities[token]
            while stack and stack[-1] != '(' and operator_priorities[stack[-1]] >= current_operator_priority:
                output.append(stack.pop())

            stack.append(token)

        else:
            raise ValueError(f"Неизвестный символ: {token}")

    while stack:
        if stack[-1] == '(':
            raise ValueError("Лишние скобки в воде")
        output.append(stack.pop())

    return output

def calculate(rpn: list) -> float:
    stack = []
    for elem in rpn:
        if is_number(elem): 
            stack.append(float(elem))
        else:

            b = stack.pop()
            a = stack.pop()
            
            if elem == '+':
                stack.append(a + b)
            elif elem == '-':
                stack.append(a - b)
            elif elem == '*':
                stack.append(a * b)
            elif elem == '/':
                stack.append(a / b)

    return stack[0]