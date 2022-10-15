# Создайте программу для игры в "Крестики-нолики".

try:
    from random import randint
    name1 = str(input("Игрок 1 введите ваше имя: "))
    name2 = str(input("Игрок 2 введите ваше имя: "))

    matrix = [["-" for j in range(3)] for i in range(3)]

    def print_matrix(matrix):
        for i in range(3): 
            print("".join(matrix[i]))

    print_matrix(matrix)

    def chek_win(matrix):
        temp = True
        for i in range(3):
            if "-" in matrix[i]:
                temp = False
        if temp:
            print("Ничья!")
            exit()
        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != "-":
                print(f"{matrix[i][0]} - победитель!")
                exit()
        for i in range(3):
            if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != "-":
                print(f"{matrix[0][i]} - победитель!")
                exit()
        if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != "-":
                print(f"{matrix[0][0]} - победитель!")
                exit()
        if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != "-":
                print(f"{matrix[0][2]} - победитель!")
                exit()

    def fill_field(flag, name):
        print(f"{name} Ваш ход. Выбирете любое пустое поле.")
        row = int(input("Введите номер строки: "))
        col = int(input("Введите номер столбца: "))
        if matrix [row-1][col-1] != "-":
            print("Эта поле уже занято.")
            fill_field(flag, name)
        else:
            matrix [row-1][col-1] = flag
            print_matrix(matrix)
            chek_win(matrix)

    def lot_motion(name1, name2):
        print("Очередность хода определяется случайным образом.")
        if randint(1, 2) == 1:
            print(f"{name1} ходит первый.")
            while True:
                fill_field("x", name1)
                fill_field("o", name2)
        else:
            while True:
                fill_field("x", name2)
                fill_field("o", name1)

    lot_motion(name1, name2)

except SystemExit:
    pass
except:
    print("Некорректный ввод. Нужно вводить цифру от 1 до 3. Попробуйте начать заново.")
    exit()