import cymysql
from config import db, host, passwd, user, user_name


def get_con():
    con = cymysql.connect(host=host, user=user, passwd=passwd, db=db)
    return con


def save_results(con, name, discarded, x1, y1, x2, y2):
    cur = con.cursor()
    values = f"{x1}, {y1}, {x2}, {y2}".replace('None', 'null')
    cur.execute(f"""INSERT INTO results (user, name, discarded, x1, y1, x2, y2) 
                    VALUES('{user_name}', '{name}', {discarded}, {values})""")
    con.commit()


def get_completed_list(con):
    cur = con.cursor()
    cur.execute(f"SELECT name from results where user = '{user_name}'") or []
    return [c[0] for c in cur.fetchall()]

