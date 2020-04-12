from flask import Flask
from flask_graphql import GraphQLView
import graphene

from models import db

from schema import Query

app = Flask(__name__)
app.debug = True

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://master:local_dev@localhost:5432/lead_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()

schema = graphene.Schema(query=Query)

# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def index():
    return '<p> Hello World!!!</p>'


if __name__ == '__main__':
    app.run()
