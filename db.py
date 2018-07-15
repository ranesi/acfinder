import os, sqlite3

SQL_FILE_NAME = 'query.sql'


def connect_db(query: str, value: int) -> list:

    conn = sqlite3.connect(os.path.join('us_areacodes.db'))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query, [value])
    ret = result.fetchall()
    conn.close()

    return ret


def get_location(value: int) -> dict:
    
    sql = get_sql_file()
    ret = connect_db(sql, value)
    return build_dict(ret)


def build_dict(r: list) -> dict:

    try:
        ret = dict(
            id=r[0][0],
            areacode=r[0][1],
            city=r[0][2],
            state=r[0][3],
            lat=r[0][5],
            lon=r[0][6])

    except IndexError:
        ret = None

    return ret


def get_sql_file() -> str:

    with open(os.path.join(SQL_FILE_NAME)) as f:
        ret = f.read()
    return ret
