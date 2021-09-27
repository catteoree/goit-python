help(tuple)

"""
Современная система оценок в университете имеет следующий вид:

Оценка	Баллы	Оценка ECTS	Объяснение
1	0-34	F	неудовлетворительно
2	35-59	FX	неудовлетворительно
3	60-66	E	достаточно
3	67-74	D	удовлетворительно
4	75-89	C	хорошо
5	90-95	В	очень хорошо
5	96-100	A	отлично

Реализуйте две функции. Первая, будет использоваться в бухгалтерии при расчете стипендии, 
get_grade, принимает ключ в оценке ECTS, 
и должна возвращать соответствующую пятибалльную оценку (первый столбик таблицы). 
Вторая get_description тоже принимает ключ в оценке ECTS, 
но будет возвращать объяснение оценки в текстовом формате (последний столбик таблицы) 
и будет использоваться в электронной зачетке студента. 
На не существующий ключ функции должны возвращать значение None

"""


def get_grade(key):
    dict_ECTS = {'F' : 1, 'FX' : 2, 'E' : 3, 'D' : 3, 'C' : 4, 'B' : 5, 'A' : 5 }
    value = dict_ECTS.get(key)

    return value 


def get_description(key):
    dict_ECTS = {'F' : 'неудовлетворительно', 'FX' : 'неудовлетворительно', 'E' : 'достаточно', 'D' : 'удовлетворительно', 'C' : 'хорошо', 'B' : 'очень хорошо', 'A' : 'отлично' }
    value = dict_ECTS.get(key)

    return value

