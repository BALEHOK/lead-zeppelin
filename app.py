import os

from flask import Flask, send_from_directory, request
from flask_graphql import GraphQLView

from src.add_lead import add_lead
from src.models import db

from src.api.schema import schema

app = Flask(__name__)
app.debug = os.getenv('DEBUG', 'True').lower() == 'true'

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                  'postgres://master:local_dev@localhost:5432/lead_collector')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()

# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


# ?account=plsch&email=asdf@zcv.ru&gc_id=33556&source=hz&content=grouppost&goal=paid_m1
@app.route('/tracking/lead', methods=["GET"])
@app.route('/tracking/lead/', methods=["GET"])
def tracking_lead():
    add_lead(request.args)
    return 'OK'


@app.route('/static/<path:path>', methods=["GET"])
def send_js(path):
    return send_from_directory('static', path)


@app.route('/', methods=["GET"])
def index():
    return '<p> Hello World!!!</p>'


if __name__ == '__main__':
    app.run()
