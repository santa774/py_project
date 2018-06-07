# coding=utf-8
from pymysql import *


def test_conn_db():
    conn = Connect(host="localhost", port=3306, user="root", passwd="233333", db="studydb", charset="utf8")
    cursor = conn.cursor()
    try:
        # insert(cursor)
        query(cursor)
    except Exception as e:
        conn.rollback()
        print("Exception: %s" % e)
    else:
        conn.commit()

    cursor.close()
    conn.close()


def insert(cursor):
    sql = "insert into student (name, gender) values ('%s', %d)"
    data = ("雷军", 1)
    cursor.execute(sql % data)


def query(cursor):
    cursor.execute("select * from trade")
    result = cursor.fetchall()
    print(result)
    # for row in cursor.fetchall():
    #     print("id: %s, name: %s, gender: %s" % row)


if __name__ == "__main__":
    test_conn_db()
