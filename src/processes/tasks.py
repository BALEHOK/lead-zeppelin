from celery.task import task

from src.processes.models import StepType, Process
from src.processes.step_interactor import StepInteractor


@task()
def step_task(process_id: str, step_id: str):
    process: Process = Process.objects(id=process_id).all_fields().first()
    if not process:
        return

    step = next(step for step in process.steps if str(step.step_id) == step_id)
    print('step', step.name)

    next_step_ids = [next_step.step_id for next_step in process.steps if next_step.prev_step_id == step.step_id]

    step_interactor = StepInteractor()
    step_interactor.execute_step(step)

    job_kwargs = {}
    if step.type == StepType.delay.name:
        job_kwargs['countdown'] = step.delay
    elif step.type == StepType.wait_until.name:
        job_kwargs['eta'] = step.when

    for next_step_id in next_step_ids:
        step_task.apply_async((process_id, next_step_id), **job_kwargs)
