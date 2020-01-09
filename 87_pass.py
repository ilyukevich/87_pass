# python3
# coding=utf-8
# 31 dec 2019 - 1 jan 2020
print("=======================")
print("""
    Программа работает с текстовым файлом '87.txt', в который помещается какой-либо произвольный текст.
    Программа берет первую текстовую строку из файла '87.txt' и помещает в список 'S1'. Текстовая строка в файле '87.txt' 
    может содержать большое количество слов. Теперь в списке 'S1' будет находится только один элемент - первая строка 
    из файла '87.txt'. 
    Далее программа выделяет и находит отдельные слова в элементе списка 'S1' и переносит их в новый список 'list0'. 
    Новый список 'list0' состоит из отдельных слов, сформированных из строки текстового файла '87.txt'.
    Отбор слов из текстовой строки 'S1' для нового списка 'list0' производится по следующим параметрам:
    ищется символ 'пробел' или символ 'точка', находится позиция этих символов, исходя из их позиции делается срез
    и слово добавляется в новый список 'list0'. Последовательность списка 'S1' сокращается на одно слово посредством
    создания новой последовательности 'S1' исключая этот срез.
    Так перебирается каждый элемент последовательности 'S1'. 
    Затем создается новый текстовый файл '87_2.txt', куда записывается новый список 'list0'. 
    Причем каждый элемент списка 'list0' - в новую строку.
    Проще говоря программа берет строку из файла '87.txt', состоящую из большого количества слов и преобразует ее 
    в отдельные слова элементы в новый файл '87_2.txt', в котором каждое слово записано в отдельной строке.
    Было:
    ["0, 1, 2, 3 , 4"] 
    Станет:
    ["0", "1", "2", "3", "4"]
        31 dec 2019 - 1 jan 2020
    """
    )
input("input 'ENTER' to start...")
f = open("87.txt", "r")
s = f.readlines()
word = " "
word2 = "."
print("Start list 'S':", s)
ln = len(s)
print("Len list 'S':", ln)
f.close()
position = -1
list0 = []
f1 = open("87.txt", "r")
s1 = f1.readline()
for i in range(ln):
    for name in s1:
        if name in word or name in word2:
            print("> position: ", position + 1, "==> DONE!")
            print("Len list 'S1':", len(s1))
            id = s1.index(name)
            print("ID return symbol: ",id)
            print("Symbol:", "'", name, "'")
            a1 = s1[:id]
            list0.append(s1[:id])
            print("Find word:", a1)
            s1 = s1[(id + 1):]
            print("Change list S1:", s1)
            print(">>> Add new list 'List0':", list0)
        else:
            position += 1
            print("> position: ", position, "==> NO!")
f1.close()
print()
print(">>>> Leng of new 'list0':", len(list0))
print()
print(">>>>>>> Write new file '87_2.txt': ")
print()
text_file = open("87_2.txt", "w")
for i in range(len(list0)):
    print(list0[i])
    text_file.write(list0[i] + "\n")
text_file.close()
print()
print(">>>>>>> Read '87_2.txt':")
print()
text_file = open("87_2.txt", "r")
print(text_file.readlines())
text_file.close()
print("=======================")
