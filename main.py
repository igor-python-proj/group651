from lessons.playlist import Playlist
from lessons.database import (
    create_tables,
    add_student,
    get_all_students
)
import sqlite3

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
    "Karakol",
)
# for st in get_all_students(connection):
#     print(st)
print("== select ==")
print(get_all_students(connection))
connection.close()