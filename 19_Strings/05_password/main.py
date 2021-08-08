def nums_and_ups(string) -> bool:
    nums = [i for i in string if i.isdigit()]
    ups = [j for j in string if j.isupper()]
    if len(nums) >= 3 and len(ups) > 0:
        return True
    else:
        return False


while True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8 and nums_and_ups(password):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадежный. Попробуйте еще раз.')
