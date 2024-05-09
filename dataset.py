import sqlite3
DB_name="population.db"
def get_conn():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def get_c1():
    conn, c = get_conn()
    sql = "select sum(population) from people " \
          "where year='2019' "
    c.execute(sql)
    d = c.fetchall()
    sql = "select population from people " \
          "where year='2019'AND country='中国' "
    c.execute(sql)
    d2 = c.fetchall()
    close_conn(conn, c)
    dd = []

    return d,d2

def get_c2():
    conn, c = get_conn()
    sql = "select country,population from people where year='2019'order by country"
    c.execute(sql)
    d = c.fetchall()
    close_conn(conn, c)
    return d

def get_l1():
    conn, c = get_conn()
    sql = "select year,sum(population) from people " \
          "group by year"
    c.execute(sql)
    d1 = c.fetchall()
    sql = "select year,sum(population) from people " \
          "where continent='亚洲'"\
          "group by year"

    c.execute(sql)
    d2 = c.fetchall()
    sql = "select year,sum(population) from people " \
          "where continent='欧洲'" \
          "group by year"

    c.execute(sql)
    d3 = c.fetchall()

    sql = "select year,sum(population) from people " \
          "where continent='非洲'"\
          "group by year"


    c.execute(sql)
    d4 = c.fetchall()

    sql = "select year,sum(population) from people " \
          "where continent='美洲'" \
          "group by year"

    c.execute(sql)
    d5 = c.fetchall()


    close_conn(conn, c)
    d = []
    i = 0
    for j in d1:
        d.append((d1[i][0], d1[i][1], d2[i][1],d3[i][1], d4[i][1],d5[i][1]))
        i += 1
    return d

def get_l2():
    conn, c = get_conn()
    sql = "select population,country from people " \
          "where year='2019'" \
          "order by population desc limit 5"
    c.execute(sql)
    d = c.fetchall()
    close_conn(conn, c)
    return d
def get_r1():
    conn, c = get_conn()
    sql = "select continent,sum(population) from people " \
          "where year='2019'" \
          "group by continent "
    c.execute(sql)
    d = c.fetchall()
    close_conn(conn, c)
    return d

print(get_r1())
