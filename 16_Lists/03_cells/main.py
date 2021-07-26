N = int(input('Количество клеток: '))
cells_list = []
for i in range(N):
    print('Какова эффективность', i + 1, 'клетки?', end=' ')
    cell_eff = int(input())
    cells_list.append(cell_eff)

unfit_cells = []

for j in range(N):
    if cells_list[j] < j:
        unfit_cells.append(cells_list[j])

print('Неподходящие значения:', end=' ')
for unfit in unfit_cells:
    print(unfit, end=' ')
