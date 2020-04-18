import time

from src.processes.models import Process, StepType


class ProcessInteractor:
    def run_for_entity(self, entity_id: str):
        for process in Process.objects(bound_entity_id=entity_id):
            self.run_step(process.id, process.first_step_id)

    def run_step(self, process_id, step_id):
        process: Process = Process.objects(id=process_id).first()
        if not process:
            return

        step = next(step for step in process.steps if step.step_id == step_id)

        if step.type == StepType.message.name:
            print(step.message)
        elif step.type == StepType.delay.name:
            time.slip(step.delay)
        elif step.type == StepType.wait_until.name:
            print('wating for', step.when)

        [self.run_step(process_id, next_step.step_id) for next_step in process.steps if
         next_step.prev_step_id == step.step_id]
