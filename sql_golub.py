import sqlite3

def create_table():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    query = """CREATE TABLE Students (
    Student_Id INTEGER NOT NULL PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL
    );"""
    cursor.execute(query)
    connection.commit()
    connection.close()
    print('Таблица создана')

def fill_table():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    query = """INSERT OR REPLACE INTO Students (Student_Id, Student_Name, School_Id)
    VALUES
    ('201', 'Иван', '1'),
    ('202', 'Петр', '2'),
    ('203', 'Анастасия', '3'),
    ('204', 'Игорь', '4'); """
    cursor.execute(query)
    connection.commit()
    connection.close()
    print('Таблица заполнена')
    
# create_table() Вызов функций закомментирован для предотвращения ошибок
# fill_table()   при повторном запуске программы
    

def get_student(student_id):
    try:
        connection = sqlite3.connect('teatchers.db')
        cursor = connection.cursor()
        select_query = """SELECT Students.Student_Id,
                          Students.Student_Name,
                          Students.School_Id,
                          School.School_Name
                          FROM Students
                          INNER JOIN School
                          ON Students.School_Id = School.School_Id
                          WHERE Student_Id = ?"""
        cursor.execute(select_query,(student_id,))
        records = cursor.fetchall()
        print ("Данные по ID студента")
        for row in records:
            print ("ID студента:", row[0])
            print ("Имя студента:", row[1])
            print ("ID школы:", row[2])
            print ("Название школы:", row[3])
        connection.close()
    except (Exception, sqlite3.Error) as error:
        print ("Ошибка в получении данных", error)
      
student_id = input('Введите ID студента: ')
get_student(student_id)
