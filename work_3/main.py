from flask import Flask, request
import sqlite3

app = Flask(__name__)


def commit_sql(sql):
    con = sqlite3.connect('phones.db')
    try:
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()


@app.route("/phones/create/")
def phones_create():
    name_value = request.args['name']
    phone_value = request.args['phone']
    if phone_value and name_value:
        sql = f'''
        INSERT INTO phones (contactName, phoneValue) VALUES ('{name_value}', '{phone_value}')
        '''
        commit_sql(sql)
    elif name_value:
        sql = f'''
        INSERT INTO phones (contactName) VALUES ('{name_value}')
        '''
        commit_sql(sql)
    else:
        sql = f'''
        INSERT INTO phones (phoneValue) VALUES ('{phone_value}')
        '''
        commit_sql(sql)

    return 'created'


@app.route('/phones/read/')
def phones_read():
    # ?name=phoneValue
    column_name = request.args.get('name', '*')
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql = f'''
        SELECT {column_name} FROM phones;
                '''
    cur.execute(sql)
    result = cur.fetchall()

    con.close()

    return str(result)


@app.route('/phones/update/')
def phones_update():
    contact_name = request.args.get('name', '')
    phone_value = request.args.get('phone', '')
    phone_id = request.args['id']

    if contact_name and phone_id:
        sql = f'''
        UPDATE phones
        SET contactName = '{contact_name}'
        WHERE phoneID = {phone_id};
        '''
        commit_sql(sql)
    elif phone_value and phone_id:
        sql = f'''
        UPDATE phones
        SET phoneValue = '{phone_value}'
        WHERE phoneID = {phone_id};
        '''
        commit_sql(sql)
    else:
        return 'enter name and id or phone and id'
    return 'phone_update'


@app.route('/phones/delete/')
def phones_delete():
    phones_id = request.args['id']

    sql = f'''
    DELETE FROM phones
    WHERE phoneID = {phones_id};
    '''
    commit_sql(sql)

    return 'phone_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)