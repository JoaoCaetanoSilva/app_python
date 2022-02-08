from datetime import date, time, datetime

def trabalhando_com_datetime():

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y' + '\n''%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_comtime():
    horario = time(hour=15, minute=17, second=54)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    trabalhando_com_date()