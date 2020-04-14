select c.name, s_from.name as from_step, s_to.name as to_step, s_cur.name as current_step, l.id as lead, h.id as history from public.clients c
    join public.leads l on c.id = l.client_id
    left join public.lead_funnel_step_history h on l.id = h.lead_id
    left join public.funnel_steps s_from on h.prev_step_id = s_from.id
    left join public.funnel_steps s_to on h.funnel_step_id = s_to.id
    left join public.funnel_steps s_cur on l.funnel_step_id = s_cur.id