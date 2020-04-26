from src.leads.models import Account, Client, db, Lead, Funnel, FunnelStep, LeadFunnelStepHistory

known_client_ids = ['vk', 'fb', 'gc', 'email', 'phone']
known_lead_markers = ['source', 'medium', 'campaign', 'content']


class LeadInteractor:
    def register_event(self, args):
        account_code = args.get('account')
        account = Account.query.filter_by(code=account_code).first()
        if account is None:
            return

        client_ids = {}
        for client_id in known_client_ids:
            val = args.get(client_id)
            if val is not None:
                client_ids[client_id] = val

        client = Client.query.filter_by(account=account, **client_ids).first()
        if client is None:
            name = args.get('name')
            client = Client(account=account, name=name, **client_ids)
            db.session.add(client)

        lead_markers = {}
        for marker in known_lead_markers:
            val = args.get(marker)
            if val is not None:
                lead_markers[marker] = val

        # ToDo refactor to allow multiple funnels per account + multiple funnels per lead
        lead = Lead.query.filter_by(client=client, **lead_markers).first()
        if lead is None:
            lead = Lead(client=client, **lead_markers)
            db.session.add(lead)

        funnel_step = FunnelStep.query.join(Funnel).filter(Funnel.account == account).filter(
            FunnelStep.code == args.get('goal')).first()
        if funnel_step is not None:
            prev_step_id = lead.funnel_step.id if lead.funnel_step is not None else None
            if (prev_step_id != funnel_step.id):
                history = LeadFunnelStepHistory(prev_step_id=prev_step_id, funnel_step_id=funnel_step.id,
                                                lead_id=lead.id)
                db.session.add(history)
                lead.funnel_step = funnel_step

        return lead
