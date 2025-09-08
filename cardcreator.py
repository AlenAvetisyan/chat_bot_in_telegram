from random import*
from math import *

def card_cr():
    foot1 = randint(1, 5)
    foot2 = randint(1, 2)
    if foot2 == 1:
        foot = 'правая'
    if foot2 == 2:
        foot = 'левая'

    skill = randint(1, 5)

    poz = randint(1, 19)
    if poz == 1:
        amplua = 'ЦЗ'
    if poz == 2:
        amplua = 'ЛЗ'
    if poz == 3:
        amplua = 'ПЗ'
    if poz == 4:
        amplua = 'ЦФД'
    if poz == 5:
        amplua = 'НАП'
    if poz == 6:
        amplua = 'ПФЗ'
    if poz == 7:
        amplua = 'ЛФЗ'
    if poz == 8:
        amplua = 'ЦОП'
    if poz == 9:
        amplua = 'ЦП'
    if poz == 10:
        amplua = 'ЦАП'
    if poz == 11:
        amplua = 'ЛП'
    if poz == 12:
        amplua = 'ПП'
    if poz == 13:
        amplua = 'ЛВ'
    if poz == 14:
        amplua = 'ПВ'
    if poz == 15:
        amplua = 'ЦП'
    if poz == 16:
        amplua = 'ЛВ'
    if poz == 17:
        amplua = 'ПВ'
    if poz == 18:
        amplua = 'НАП'
    if poz == 19:
        amplua = 'ЦЗ'

    pace = randint(22, 99)
    sho = randint(22, 99)
    pas = randint(22, 99)
    dri = randint(22, 99)
    defend = randint(22, 99)
    phy = randint(22, 99)
    ovr1 = pace + sho + pas + dri + defend + phy
    ovr2 = round(ovr1 / 5)
    ves = randint(49, 100)
    rost = randint(130, 219)
    vozrast = randint(10, 52)

    data = f'''
    Позиция: {amplua} 
    Овр: {ovr2} 
    Скорость: {pace} 
    Удары: {sho} 
    Пасы: {pas} 
    Дриблинг: {dri} 
    Защита: {defend} 
    Физ подготовка: {phy} 
    Вес: {ves} 
    Рост: {rost}
    Возраст: {vozrast} 
    Финты: {skill} 
    Рабочая нога: {foot} 
    Нерабочая нога: {foot1}'''
    return data
