from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y' + '\n' + '%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=17, second=54)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    # Obs: Se fizer assim: Tira os mili-segundos:
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo']
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2022, 2, 8, 17, 58, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '08/02/2022 18:52:6'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=20, minutes=5)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()