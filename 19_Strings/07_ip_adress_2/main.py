def check_ip(ip):
    ip_list = ip.split('.')

    for k in range(len(ip_list)):
        if not ip_list[k].isdigit():
            return '{} - не целое число'.format(ip_list[k])
        if not 0 <= int(ip_list[k]) <= 255:
            return '{} находится за пределами [0;255]'.format(ip_list[k])
        if len(ip_list) != 4:
            return 'Адрес - это четыре числа, разделенные точкой'


your_ip = input('Введите IP: ')
print(check_ip(your_ip))
