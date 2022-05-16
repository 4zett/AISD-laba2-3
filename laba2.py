import os
import re
import time

work_buffer = ''
fin_buffer = ''
buffer_len = 1
flag = False
flag2 = False
h = 0
try:
    print("\n ___  Результат работы программы  ___ ")
    print("\n ___  Локальное время", time.ctime()," ___ \n")
    with open('laboratornaya2.txt', 'r') as file:   #открываем файл
        buffer = file.read(buffer_len)  #считываем символ из файла
        start = time.time()
        if not buffer:
            print('\nРабочий файл пустой, измените содержимое файла')   #если в файле нет символов
        while buffer:
            if re.findall(r'["]', buffer) and not flag2:    #поиск ковычек
                work_buffer += buffer   #запись конечного результата
                buffer = file.read(buffer_len)  #чтение следующего символа
                flag = True
                flag2 = True
                h += 1
            if re.findall(r'[\w\s\S,;:^"]', buffer) and flag:   #вывод всех символов после ковычек
                work_buffer += buffer
            if re.findall(r'["]', buffer) and flag: #поиск последних ковычек в цитате
                work_buffer += buffer
                print(work_buffer[:-1])     #вывод конечного результата
                work_buffer = ""    #обнуление конечной переменной
                flag = False
                flag2 = False
            buffer = file.read(buffer_len)      #чтение следующего символа
        finish = time.time()
        result = finish - start
        print("\nProgram time: " + str(result) + " seconds.")
        print("Program size: " + str(os.path.getsize('laba2.py')) + " bytes.")
        if h == 0 and buffer:   #проверка на наличие ковычек
            print('\nВ тексте отсутствуют цитаты.')     #вывод в случае отсутствия ковычек
except FileNotFoundError:
    print('\nФайл laboratornaya2.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий')     #вывод в случае если нет файла