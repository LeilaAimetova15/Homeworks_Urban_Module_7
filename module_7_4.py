team1_num = 5 #команда мастера кода
team2_num = 6 #команда волшебники данных
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 18015.3
tasks_total = 82
time_avg = 350.4
challenge_result = 'Победа команды Волшебники данных!'
#Использование %:
print('В команде Мастера кода участников: %s ! ' % team1_num)
print('Итого сегодня в командах участников: %s и %s ' % (team1_num, team2_num))
#Использование format():
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач,', f'в среднем по {time_avg} секунды на задачу!')