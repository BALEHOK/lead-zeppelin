from src.leads.models import Payment, db


class PaymentInteractor:
    def add_payment(self, client, paid, parse_price):
        if parse_price:
            try:
                paid = int(paid.split()[0]) * 100
            except:
                return None

        payment = Payment(client_id=client.id, amount_paid=paid)
        db.session.add(payment)
        return payment

    def add_leads_payment(self, lead, paid, parse_price):
        payment = self.add_payment(lead.client, paid, parse_price)

        payment.lead_id = lead.id
        payment.funnel_step_id = lead.funnel_step_id

        return payment
