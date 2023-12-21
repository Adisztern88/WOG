
def write_name(name):
    my_file = open('names.txt', 'a')
    my_file.write(f'{name}\n')
    my_file.close()

def read_namse():
    my_file = open('names.txt')
    for name in my_file.readlines():
        print(f'Hi {name.strip()}, and welcome')

write_name('doron')
write_name('noga')
write_name('tal')
read_namse()