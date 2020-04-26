from src.leads.models import Payment, db


class PaymentInteractor:
    def add_payment(self, client, paid):
        payment = Payment(client_id=client.id, amount_paid=paid)
        db.session.add(payment)
        return payment

    def add_leads_payment(self, lead, paid):
        payment = self.add_payment(lead.client, paid)

        payment.lead_id = lead.id
        payment.funnel_step_id = lead.funnel_step_id

        return payment
