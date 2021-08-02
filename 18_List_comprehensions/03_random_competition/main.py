from random import uniform

team_1 = [round(uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(uniform(5, 10), 2) for _ in range(20)]
contest_results = [team_1[member] if team_1[member] > team_2[member]
                   else team_2[member] for member in range(20)]
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', contest_results)