import pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize #Импортируем нужные модуля

#Организуем бесконечный цикл
while True:
    ans = input('Для завершения работы введите 1\n')
    if ans == '1':
        break
    try:

        answer = int(input('Введите количество переменных\n'))

        variable = []
        #При помощи функции LpVariable инициализируем используемые в вычисления переменные
        for i in range(answer):
               exec(f'y{str(i+1)} = LpVariable(name="y{str(i+1)}", lowBound=0, cat="Float")')

        answer = int(input('Введите количество целевых функций\n'))

        functions = []
        maxormin = []
        #Добавляем функции, которые в дальнейшем будем вычислять
        for i in range(answer):
            functions.append(input("Введите функцию (в качестве неизвестной введите yi)\n"))
            maxormin.append(input("Введите стремление функции(max или min)\n"))




        answer = int(input('Введите количество ограничений\n'))
        nonfunc = []

        #Добавляем ограничения и форматируем их для работы с библиотекой pulp
        for i in range(answer):
              nonfunc.append('('+input("Введите ограничение(в качестве неизвестной введите yi)\n")+', "'+str(i)+'" )')
              print(nonfunc[i])
        count = 0


        while count < len(functions):
            model = object
            #В зависимости от стремления вычисляемой функции выбираем минимизацию её или максимизацию
            if maxormin[count] == 'max':
                model = LpProblem(name="small-problem", sense=LpMaximize)
            else:
                model = LpProblem(name="small-problem", sense=LpMinimize)
            print('Non func')
            #Добавляем в модель ограничения
            for i in nonfunc:
                model += eval(i)
            print('Non func')
            #Добавляем в модель вычисляемую функцию
            model += lpSum([eval(functions[count])])
            print('LpSum')
            #Производим вычисление модели
            model.solve()
            print('model')

            #Выводим нужные результаты
            print(f"objective: {model.objective.value()}")

            for var in model.variables():
                print(f"{var.name}: {var.value()}")
            for name, constraint in model.constraints.items():
                print(f"{name}: {constraint.value()}")

            answer = int(input('Введите уступку\n'))

            #При следующем вычислении функция, будет использоваться как ограничение
            if maxormin[count] == 'max':
                nonfunc.append('(' + functions[count] + ' >= ' + str(model.objective.value() - answer) + ', "' + str(len(functions)+1)+'" )')
            else:
                nonfunc.append('(' + functions[count] + ' <= ' + str(model.objective.value() - answer) + ', "' + str(len(functions)+1) + '" )')
            # print(nonfunc[0])
            # print(nonfunc[-1])
            count +=1


            # print(f"status: {model.status}, {LpStatus[model.status]}")

            # print(f"objective: {model.objective.value()}")
            #
            # for var in model.variables():
            #     print(f"{var.name}: {var.value()}")
            #
            # for name, constraint in model.constraints.items():
            #     print(f"{name}: {constraint.value()}")
    except:
        print('Произошла непредвиденная ошибка!\n')


