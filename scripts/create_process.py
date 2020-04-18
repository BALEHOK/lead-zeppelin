# from scripts.create_process import create_process
from mongoengine import connect

from src.processes.models import ProcessStepMessage, Process
from src.processes.process_interactor import ProcessInteractor


def create_process():
    connect(host='mongodb://localhost:27017/lead_zeppelin_dev')

    step1 = ProcessStepMessage(name="Step 1", message="Hello man!")
    step2 = ProcessStepMessage(name="Step 2", message="Welcome to Lead Zeppelin", prev_step_id=step1.step_id)
    process = Process(bound_entity_id="1", name="first process", first_step_id=step1.step_id, steps=[step1, step2])

    process.save()

def run_process():
    connect(host='mongodb://localhost:27017/lead_zeppelin_dev')
    process_interactor = ProcessInteractor()
    process_interactor.run_for_entity('1')

run_process()
