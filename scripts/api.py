import flask
from flask import request, jsonify
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'myroot'
app.config['MYSQL_DB'] = 'tg_rl_openai_atari'

mysql = MySQL(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Aprendizagem por reforço utilizando Q-Learning em jogos eletrônicos de ATARI</h1>
<p>API para executar e armazer o treinamento e visualizar os resultados.</p>'''


@app.route('/api/v1/resources/games/all', methods=['GET'])
def api_all_games():
    try:
        all_games = []
        query = 'SELECT * FROM games;'
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        all_games = cur.fetchall()
        cur.close()
        return jsonify(all_games)
    except Exception as e:
        return e

@app.route('/api/v1/resources/games', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()