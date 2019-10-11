def digit_count():
    num = [int(i) for i in text if i.isdigit()]
    digitdict = {'Количество цифр в тексте': len(num)}
    return digitdict


def line_count():
    thislinedict = dict.fromkeys(['Количество строк'], thisnumberlist[0])
    return thislinedict


def word_count():
    thisworddict = dict(zip(text6, thisnumberlist2))
    return thisworddict


def char_count():
    thischardict = dict(zip(text3, thisnumberlist))
    return thischardict


def text_stat():
    ndic = {**digit_count(), **line_count(), **char_count(), **word_count()}
    return ndic


def text_print0():
    ndic1 = {'==== Открытие': 'словаря = символов  ===='}
    linedigetprint = {**digit_count(), **line_count(), **ndic1}
    return linedigetprint


def text_sepr():
    seprdict = {'==== Закрытие': 'словаря = символов ====\n', '==== Открытие': 'словаря = слов ===='}
    return seprdict


def text_sepr2():
    ndic2 = {'==== Закрытие': 'словаря = слов ===='}
    return ndic2
text = ""
stopword = ""
while True:
    line = input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line

thisnumberlist = []
thisnumberlist2 = []

text = text.casefold()                          # text case fold
text1 = list(text)                              # text1 необходим для функции digit_count
text2 = set(text1)                              # text 2 множество
text3 = list(text2)                             # text 3 список
text3.sort()                                    # text 3 сортирований список

text4 = text.replace("\n", " ")                 # text 4 строка без спец символов
text4 = text4.split(" ")                        # text 4 список слов
text4.remove("")                                # text 4 убрали пустую строку
text5 = set(text4)                              # text 5 множество слов
text6 = list(text5)                             # text 6 список слов
text6.sort()                                    # text 6 Сортированый список слов

for x in text3:
    thisnumberlist.append(text.count(x))

for x in text6:
    thisnumberlist2.append(text4.count(x))

for y in text_print0():                         # Начало вывода текста для пользователя
    print(y, '=', text_print0()[y])

for i in char_count():
    print({i}, '=', char_count()[i])

for y in text_sepr():
    print(y, '=', text_sepr()[y])

for i in word_count():
    print({i}, '=', word_count()[i])

for y in text_sepr2():
    print(y, '=', text_sepr2()[y])


#Работали над этим ВЕЛОСИПЕДИЩЕМ вместе с Константиновым. Готовы к правкам.
