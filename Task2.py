#print(eval("((2+3)*5+(3-2))*6"))
# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.

# Задача решена с использованием метода ОПЗ (обратная польская запись). Добавлена возможность возведения в степень (символ ^). 
# Ссылка на описание https://temofeev.ru/info/articles/algoritm-vychisleniya-arifmeticheskogo-vyrazheniya-v-vide-stroki/
# Программа не чувствительна к наличию пробелов. 
# В try-except не стал заворачивать))) Если правильное выражение, то считает корректно, в том числе и вложенные скобки.

expression = input("Введите математическое выражение: ")

def preparation(expression):
    count = 1
    while " " in expression:
        expression = expression.replace(" ", "")
    expression = list(expression)
    while count < len(expression):
        if expression[count].isdigit() and expression[count-1].isdigit():
            expression[count-1] = expression[count-1] + expression[count]
            expression.pop(count)
        else:
            count += 1
    return expression

def priority(oper):
    if oper == '*':
        return 2
    elif oper == '/':
        return 2
    elif oper == '+':
        return 1
    elif oper == '-':
        return 1
    elif oper == '(':
        return 0
    elif oper == '^':
        return 3

def opz(expression):
    result=[]
    oper_stack=[]
    for i in expression:
        if i.isdigit():
            result.append(int(i)) 
        elif i in ['*','/','+','-','^']:
            token_tmp = ''
            if len(oper_stack) > 0:
                token_tmp = oper_stack[len(oper_stack) - 1]
                while (len(oper_stack) > 0 and token_tmp != '('):
                    if (priority(i) <= priority(token_tmp)):
                        result.append(oper_stack.pop())
                        token_tmp = oper_stack[len(oper_stack) - 1]
                    else:
                        break     
            oper_stack.append(i)
        elif i == '(':
            oper_stack.append(i)
        elif i == ')':
            token_tmp = oper_stack[len(oper_stack) - 1]
            while token_tmp != '(':
                result.append(oper_stack.pop())
                token_tmp = oper_stack[len(oper_stack) - 1]              
                if len(oper_stack) == 0:
                    raise RuntimeError('V virajenii propushena (') 
                if token_tmp == '(':
                    oper_stack.pop()
    while len(oper_stack) > 0:
        result.append(oper_stack.pop())
    return result

def count_opz(list):
    final_result = []
    for item in list:
        if type(item) == (int or float):
            final_result.append(item)
        else:
            left_oper = final_result.pop()
            right_oper = final_result.pop()
            if item == "-":
                final_result.append(right_oper - left_oper)
            elif item == "+":
                final_result.append(right_oper + left_oper)
            elif item == "*":
                final_result.append(right_oper * left_oper)
            elif item == "/":
                final_result.append(right_oper / left_oper)
            elif item == "^":
                final_result.append(right_oper ** left_oper)
    return final_result[0]

print(f"{expression} = {count_opz(opz(preparation(expression)))}")