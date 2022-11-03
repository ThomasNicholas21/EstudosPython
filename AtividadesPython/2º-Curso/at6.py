from datetime import date, time, datetime, timedelta
from pip import main


def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime('%d/%m/%Y  %H:%M:%S')
    print(data_atual_str)
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terca', 'Quarta',
             'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    nova_data = data_atual - timedelta(days=365)
    print(nova_data.strftime('%d/%m/%Y'))


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d %m %Y')
    print(data_atual)
    print(type(data_atual_str))
    print(data_atual_str)


def trabalhando_com_time():
    horario = time(hour=14, minute=40, second=30)
    horario2 = horario.strftime('%H %M %S')
    print(horario2)


if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
