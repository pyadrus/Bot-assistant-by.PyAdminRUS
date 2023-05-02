# import math

from aiogram.dispatcher.filters.state import StatesGroup, State

jan = 'Январь 23'
feb = 'Февраль 23'
mar = 'Март 23'
apr = 'Апрель 23'
may = 'Май 23'
june = 'Июнь 23'
jul = 'Июль 23'
aug = 'Август 23'
sep = 'Сентябрь 23'
oct = 'Октябрь 23'
nov = 'Ноябрь 23'
dec = 'Декабрь 23'


class Form(StatesGroup):
    month = State()
    district = State()
