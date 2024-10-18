from aiogram.fsm.state import StatesGroup, State

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

jan = 'Январь 23'
feb = 'Февраль 23'
mar = 'Март 23'
apr = 'Апрель 23'
may = 'Май 23'
june = 'Июнь 23'
jul = 'Июль 23'
aug = 'Август 23'
sep = 'Сентябрь 23'
oct_23 = 'Октябрь 23'
nov = 'Ноябрь 23'
dec = 'Декабрь 23'

jan_2024 = 'Январь 24'
feb_2024 = 'Февраль 24'
mar_2024 = 'Март 24'
apr_2024 = 'Апрель 24'
may_2024 = 'Май 24'
june_2024 = 'Июнь 24'
jul_2024 = 'Июль 24'
aug_2024 = 'Август 24'
sep_2024 = 'Сентябрь 24'
oct_2024 = 'Октябрь 24'
nov_2024 = 'Ноябрь 24'
dec_2024 = 'Декабрь 24'


class Form(StatesGroup):
    month = State()
    district = State()


class Form_2024(StatesGroup):
    month_2024 = State()
    district_2024 = State()
