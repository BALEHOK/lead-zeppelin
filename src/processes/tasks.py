from uuid import UUID

from celery.task import task

from src.processes.models import StepType, Process
from src.processes.step_interactor import StepInteractor


@task()
def step_task(process_id: str, step_id: UUID):
    process: Process = Process.objects(id=process_id).first()
    if not process:
        return

    step = next(step for step in process.steps if step.step_id == step_id)

    step_interactor = StepInteractor()
    step_interactor.execute_step(step)

    job_kwargs: dict
    if step.type == StepType.delay.name:
        job_kwargs = {'countdown': step.delay}
    elif step.type == StepType.wait_until.name:
        job_kwargs = {'eta': step.when}

    [step_task.apply_async((process_id, next_step.step_id), kwargs=job_kwargs) for next_step in process.steps if
     next_step.prev_step_id == step.step_id]


# def step_job(process_id: str, step_id: UUID):
#     process: Process = Process.objects(id=process_id).first()
#     if not process:
#         return
#
#     step = next(step for step in process.steps if step.step_id == step_id)
#
#     step_interactor = StepInteractor()
#     step_interactor.execute_step(step)
#
#     [step_job(process_id, next_step.step_id) for next_step in process.steps if
#      next_step.prev_step_id == step.step_id]
