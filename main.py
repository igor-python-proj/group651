from lessons.playlist import Playlist
from lessons.database import (
    create_tables,
    add_student,
    get_all_students,
    get_one_student,
    get_students_by_name,
    delete_student,
    delete_by_city,
    change_student
)
import sqlite3
from colorama import Fore

# play = Playlist("pop-2")
# print(play)
connection = sqlite3.connect('database.db')
create_tables(connection)
add_student(
    connection,
    "Igor",
    35,
    "Bishkek",
)
add_student(
    connection,
    "Kurmanbek",
    20,
    "Bishkek",
)
add_student(
    connection,
    "Akylay",
    21,
    "Bishkek",
)
add_student(
    connection,
    "Burul",
    22,
    "Karakol",
)
add_student(
    connection,
    "Kubat",
    23,
    "Naryn",
)
# for st in get_all_students(connection):
#     print(st)
print("== select ==")
print(get_all_students(connection))
one_student = get_one_student(
    connection, 2
)
print(one_student)
by_name = get_students_by_name(
    connection, "Kurmanbek"
)
print(by_name)


print("== delete ==")
delete_student(connection, 1)
print(get_all_students(connection))
print("---")
delete_by_city(connection, "Bishkek")
print(get_all_students(connection))

print("== update ==")
change_student(
    connection,
    4,
    "Burul",
    21,
    "Naryn",
)
print(Fore.RED + 'some red text')
print(get_one_student(connection, 4))
connection.close()

