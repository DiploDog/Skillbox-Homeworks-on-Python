N = int(input('Количество видеокарт: '))
gpu_list = []
max_x_gpu = 0
for i in range(N):
    print(i + 1, 'Видеокарта:', end=' ')
    x_gpu = int(input())
    gpu_list.append(x_gpu)
    if x_gpu > max_x_gpu:
        max_x_gpu = x_gpu

new_gpu_list = []
for j in gpu_list:
    if j < max_x_gpu:
        new_gpu_list.append(j)

print('\nСтарый список видеокарт:', gpu_list)
print('Новый список видеокарт:', new_gpu_list)