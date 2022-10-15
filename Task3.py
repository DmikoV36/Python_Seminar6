# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# 
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Порядок вывода команд произвольный.

with open('file.txt', 'r') as data:
    lines = data.readlines()

data = []
def preparation_data(lines):
    for i in range(1, len(lines)):
        if '\n' in lines[i]:
            lines[i] = lines[i][:-1]
        data.append(lines[i].split(';'))
    return data

def create_table(data):
    teams = set()
    for i in range(len(data)):
        teams.update([data[i][0], data[i][2]])
    teams = list(teams)
    for i in range(len(teams)):
        teams[i] = [teams[i], 0, 0, 0, 0, 0]
    return teams


def fill_table (data,teams):
    for i in range(len(data)):
        for j in range(len(teams)):
            if data[i][1] < data[i][3]:
                if data[i][0] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][2] += 1
                    teams[j][5] += 3
                if data[i][2] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][4] += 1
            elif data[i][1] > data[i][3]:
                if data[i][0] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][4] += 1
                if data[i][2] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][2] += 1
                    teams[j][5] += 3
            elif data[i][1] == data[i][3]:
                if data[i][0] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][3] += 1
                    teams[j][5] += 3
                if data[i][2] == teams[j][0]:
                    teams[j][1] += 1
                    teams[j][3] += 1
                    teams[j][5] += 3
    return teams                

def print_table(teams):
    for i in range(len(teams)):
        print(f"{teams[i][0]}:{teams[i][1]} {teams[i][2]} {teams[i][3]} {teams[i][4]} {teams[i][5]}")

preparation_data(lines)
print_table(fill_table(data, create_table(data)))