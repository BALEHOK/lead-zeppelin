from flask import Flask, send_from_directory, request
from flask_graphql import GraphQLView
# from mongoengine import connect

from src.config import config
from src.leads.lead_interactor import LeadInteractor
from src.leads.models import db

from src.web.schema import schema
# from src.leads.payment_interactor import PaymentInteractor
# from src.processes.process_interactor import ProcessInteractor

web_app = Flask(__name__)
web_app.debug = config.get('debug')
web_app.config['SQLALCHEMY_DATABASE_URI'] = config.get('sql_db_url')
web_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with web_app.app_context():
    db.init_app(web_app)

# connect(host=config.get('mongo_web_uri'))

# Routes
web_app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


# ?account=plsch&email=asdf@zcv.ru&gc_id=33556&source=hz&content=grouppost&goal=paid_m1
@web_app.route('/tracking/lead', methods=["GET"])
@web_app.route('/tracking/lead/', methods=["GET"])
def tracking_lead():
    lead_interactor = LeadInteractor()
    lead = lead_interactor.register_event(request.args)

    # amount_paid = request.args.get('paid')
    # if (amount_paid):
    #     payment_interactor = PaymentInteractor()
    #     payment_interactor.add_leads_payment(lead, amount_paid)

    db.session.commit()

    # process_interactor = ProcessInteractor()
    # process_interactor.run_for_entity(str(lead.funnel_step_id))

    return 'OK'


@web_app.route('/static/<path:path>', methods=["GET"])
def send_js(path):
    return send_from_directory('static', path)


@web_app.route('/', methods=["GET"])
def index():
    return '<p> Hello World!!!</p>'


if __name__ == '__main__':
    port = config.get('web_port')
    web_app.run(host='0.0.0.0', port=port)
