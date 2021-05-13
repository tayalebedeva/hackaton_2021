import matplotlib.pyplot as plt
import numpy as numpy

birds = open('C:\\Users\\Опа)\\Desktop\\bird.csv', 'r')
#функция для создания графиков
def scatterplot(x_data='', y_data='',x_label='', y_label='', title='', size='',color='black'):
    fiх,ax = plt.subplots()
    for i in range(0,len(size)):
        size[i]=size[i]*1000
    ax.scatter(x_data, y_data, s = size, color=color, alpha = 0.4)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()
#функция создания из общего массива отдельные массивы столбцов
def str_in_arr(string):
    sub_arr = string.split(',')
    arr =[]
    arr.append(int(sub_arr[0]))

    for i in range(1,len(sub_arr)-1):
        if(sub_arr[i]):
            arr.append(float(sub_arr[i]))
        else:
            return 'null'
    arr.append(sub_arr[len(sub_arr)-1])
    global animalsDict
    animalsDict[sub_arr[len(sub_arr)-1]]+=1
    arr.append(animalsDict[sub_arr[len(sub_arr)-1]])
    
    return arr
#===============================================================
#общий массив
birds_arr = []
#массивы столбцов
huml_arr = []
humw_arr = []
ulnal_arr = []
ulnaw_arr = []
feml_arr = []
femw_arr = []
tibl_arr = []
tibw_arr = []
tarl_arr = []
tarw_arr = []
x_arr=[]
color_arr=[]

#словарь для определения координаты x
animalsDict ={
    'SW': 0,
    'W': 0,
    'T': 0,
    'R': 0,
    'P': 0,
    'SO': 0
    }

#формирование общего массива
flag = 0
for line in birds:
    if(flag != 0):
        line = line.rstrip()
        sub_arr = str_in_arr(line)
        if(sub_arr != 'null'):
            birds_arr.append(sub_arr)
    else:
        flag = 1
        
#формирование массивов столбцов
for i in range(0,len(birds_arr)):
    huml_arr.append(birds_arr[i][1])
    humw_arr.append(birds_arr[i][2])
    ulnal_arr.append(birds_arr[i][3])
    ulnaw_arr.append(birds_arr[i][4])
    feml_arr.append(birds_arr[i][5])
    femw_arr.append(birds_arr[i][6])
    tibl_arr.append(birds_arr[i][7])
    tibw_arr.append(birds_arr[i][8])
    tarl_arr.append(birds_arr[i][9])
    tarw_arr.append(birds_arr[i][10])
    x_arr.append(birds_arr[i][12])
    #массив цветов
    if(birds_arr[i][11] == 'SW'):
        color_arr.append('green')
    if(birds_arr[i][11] == 'W'):
        color_arr.append('red')
    if(birds_arr[i][11] == 'T'):
        color_arr.append('blue')
    if(birds_arr[i][11] == 'R'):
        color_arr.append('yellow')
    if(birds_arr[i][11] == 'P'):
        color_arr.append('pink')
    if(birds_arr[i][11] == 'SO'):
        color_arr.append('grey')
        
#построение графиков
scatterplot(x_arr,huml_arr,'Количество особей','Длина плечевой кости,мм','Плечевая кость',humw_arr,color_arr)
scatterplot(x_arr,ulnal_arr,'Количество особей','Длина локтевой кости,мм','Локтевая кость',ulnaw_arr,color_arr)
scatterplot(x_arr,feml_arr,'Количество особей','Длина бедренной кости,мм','Бедренная кость',femw_arr,color_arr)
scatterplot(x_arr,tibl_arr,'Количество особей','Длина тибиотарзуса,мм','Тибиотарзус',tibw_arr,color_arr)
scatterplot(x_arr,tarl_arr,'Количество особей','Длина предплюсны,мм','Предплюсна',tarw_arr,color_arr)

#медианные значения
huml_median = numpy.median(huml_arr)
humw_median = numpy.median(humw_arr)
ulnal_median = numpy.median(ulnal_arr)
ulnaw_median = numpy.median(ulnaw_arr)
feml_median = numpy.median(feml_arr)
femw_median = numpy.median(femw_arr)
tibl_median = numpy.median(tibl_arr)
tibw_median = numpy.median(tibw_arr)
tarl_median = numpy.median(tarl_arr)
tarw_median = numpy.median(tarw_arr)

print('Медианное значение длины плечевой кости,мм=',huml_median)
print('Медианное значение диаметра плечевой кости,мкм=',humw_median)
print('Медианное значение длины локтевой кости,мм=',ulnal_median)
print('Медианное значение диаметра локтевой кости,мкм=',ulnaw_median)
print('Медианное значение длины бедренной кости,мм=',feml_median)
print('Медианное значение диаметра бедренной кости,мкм=',femw_median)
print('Медианное значение длины тибиотарзуса,мм=',tibl_median)
print('Медианное значение диаметра тибиотарзуса,мкм=',tibw_median)
print('Медианное значение длины предплюсны,мм=',tarl_median)
print('Медианное значение диаметра предплюсны,мкм=',tarw_median)

# средние значения
huml_mean = numpy.mean(huml_arr)
humw_mean = numpy.mean(humw_arr)
ulnal_mean = numpy.mean(ulnal_arr)
ulnaw_mean = numpy.mean(ulnaw_arr)
feml_mean = numpy.mean(feml_arr)
femw_mean = numpy.mean(femw_arr)
tibl_mean = numpy.mean(tibl_arr)
tibw_mean = numpy.mean(tibw_arr)
tarl_mean = numpy.mean(tarl_arr)
tarw_mean = numpy.mean(tarw_arr)

print('Среднее значение длины плечевой кости,мм=',huml_mean)
print('Среднее значение диаметра плечевой кости,мкм=',humw_mean)
print('Среднее значение длины локтевой кости,мм=',ulnal_mean)
print('Среднее значение диаметра локтевой кости,мкм=',ulnaw_mean)
print('Среднее значение длины бедренной кости,мм=',feml_mean)
print('Среднее значение диаметра бедренной кости,мкм=',femw_mean)
print('Среднее значение длины тибиотарзуса,мм=',tibl_mean)
print('Среднее значение диаметра тибиотарзуса,мкм=',tibw_mean)
print('Среднее значение длины предплюсны,мм=',tarl_mean)
print('Среднее значение диаметра предплюсны,мкм=',tarw_mean)

#максимумы и минимумы
huml_max = max(huml_arr)
humw_max = max(humw_arr)
ulnal_max = max(ulnal_arr)
ulnaw_max = max(ulnaw_arr)
feml_max = max(feml_arr)
femw_max = max(femw_arr)
tibl_max = max(tibl_arr)
tibw_max = max(tibw_arr)
tarl_max = max(tarl_arr)
tarw_max = max(tarw_arr)

huml_min = min(huml_arr)
humw_min = min(humw_arr)
ulnal_min = min(ulnal_arr)
ulnaw_min = min(ulnaw_arr)
feml_min = min(feml_arr)
femw_min = min(femw_arr)
tibl_min = min(tibl_arr)
tibw_min = min(tibw_arr)
tarl_min = min(tarl_arr)
tarw_min = min(tarw_arr)

print('Максимум и минимум длины плечевой кости=',huml_max,'мм,',huml_min,'мкм')
print('Максимум и минимум диаметра плечевой кости=',humw_max,'мм,',humw_min,'мкм')
print('Максимум и минимум длины локтевой кости=',ulnal_max,'мм,',ulnal_min,'мкм')
print('Максимум и минимум диаметра локтевой кости=',ulnaw_max,'мм,',ulnaw_min,'мкм')
print('Максимум и минимум длины бедренной кости=',feml_max,'мм,',feml_min,'мкм')
print('Максимум и минимум диаметра бедренной кости=',femw_max,'мм,',femw_min,'мкм')
print('Максимум и минимум длины тибиотарзуса=',tibl_max,'мм,',tibl_min,'мкм')
print('Максимум и минимум диаметра тибиотарзуса=',tibw_max,'мм,',tibw_min,'мкм')
print('Максимум и минимум длины предплюсны=',tarl_max,'мм,',tarl_min,'мкм')
print('Максимум и минимум диаметра предплюсны=',tarw_max,'мм,',tarw_min,'мкм')

#подсчет количества птиц
print(animalsDict)