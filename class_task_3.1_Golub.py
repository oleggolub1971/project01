# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.
class Matrix(list):
    def __init__(self):
        self.matrix = []
        row = []
        n = int(input('Введите высоту матрицы: '))
        m = int(input('Введите ширину матрицы: '))
        val = int(input('Введите значение для заполнения матрицы: '))
        for i in range(n):
            self.matrix.append([0]*m)
        
        for i in range(len(self.matrix)): # заполняем матрицу введенным значением val
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = val
                
        for i in range(len(self.matrix)): # вывод матрицы
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end = ' ')
            print()

    
    def get_matrix(self): # функция вывода матрицы
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end = ' ')
            print()

            
    def replace_value(self, i, j, val): # функция замены отдельных значений
        self.matrix[i][j] = val

                
    def size_matrix(self):
        print('Количество строк матрицы:', len(self.matrix))
        print('Количество столбцов матрицы:', len(self.matrix[0]))

               
    def new_rows(self): # функция добавления новых строк матрицы внизу
        add_rows = int(input('Введите количество дополнительных строк: '))
        row_val = int(input('Введите значение для заполнения новых строк: '))
        row = []
        for i in range(len(self.matrix)):
            row.append(row_val)
        for i in range(add_rows):
            self.matrix.append(row)
            
    def new_columns(self): # функция добавления новых столбцов в конце
        add_columns = int(input('Введите количество дополнительных столбцов: '))
        column_val = int(input('Введите значение для заполнения новых столбцов: '))
        for i in range(len(self.matrix)):
            for j in range(add_columns):
                self.matrix[i].append(column_val)

    def del_row(self): # функция удаления строки
        row_num = int(input('Введите номер строки, которую нужно удалить '))
        del self.matrix[row_num]

    def del_column(self): # функция удаления столбца
        row_col = int(input('Введите номер столбца, который нужно удалить '))
        for i in range(len(self.matrix)):
            del self.matrix[i][row_col]

    def insert_row(self): # функция добавления новой строки в определенное место
        row_pos = int(input('Введите позицию, в которой нужно вставить строку: '))
        row_val = int(input('Введите значение для заполнения новой строки: '))
        row = []
        for i in range(len(self.matrix)):
            row.append(row_val)
        self.matrix.insert(row_pos, row)

    def insert_col(self): # функция добавления нового столбца в определенное место
        col_pos = int(input('Введите позицию, в которой нужно вставить столбец: '))
        col_val = int(input('Введите значение для заполнения нового столбца: '))
        for i in range(len(self.matrix)):
            self.matrix[i].insert(col_pos, col_val)
     
k = Matrix() # создаем и выводим матрицу нужного размера
print()

k.replace_value(1, 1, 8) # заменяем второе значение во второй строке на 8
k.get_matrix() # выводим результат
print()

k.size_matrix() # выводим размеры матрицы
print()

k.new_rows() # добавляем новые строки внизу
k.get_matrix() # выводим результат
print()

k.new_columns() # добавляем новые столбцы в конце
k.get_matrix() # выводим результат
print()

k.del_row() # удаляем строку
k.get_matrix() # выводим результат
print()

k.del_column() # удаляем столбец
k.get_matrix() # выводим результат
print()

k.insert_row() # вставляем столбец
k.get_matrix() # выводим результат
print()

k.insert_col() # вставляем строку
k.get_matrix() # выводим результат

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)
