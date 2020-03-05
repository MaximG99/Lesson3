#Задание
#Скачайте файл по ссылке
#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt 

with open("referat.txt", "r", encoding="utf-8") as f:
     content = f.read()
content = content.replace(".","!")

with open("referat2.txt","w", encoding="utf-8") as d:
    d = d.write(content)   


def findLen(content):

    counter = 0    

    for i in content:

        counter += 1

    return counter

  
print(content)
print(findLen(content))
print(len(content.split()))