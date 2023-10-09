# import math

from aiogram.dispatcher.filters.state import StatesGroup, State

jan_22 = 'Январь 22'
feb_22 = 'Февраль 22'
mar_22 = 'Март 22'
apr_22 = 'Апрель 22'
may_22 = 'Май 22'
june_22 = 'Июнь 22'
jul_22 = 'Июль 22'
aug_22 = 'Август 22'
sep_22 = 'Сентябрь 22'
oct_22 = 'Октябрь 22'
nov_22 = 'Ноябрь 22'
dec_22 = 'Декабрь 22'


class Form(StatesGroup):
    month = State()
    district = State()
