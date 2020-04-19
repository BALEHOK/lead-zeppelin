from src.processes.models import Process
from .tasks import step_task


class ProcessInteractor:
    @staticmethod
    def run_for_entity(entity_id: str):
        for process in Process.objects(bound_entity_id=entity_id):
            step_task.delay(str(process.id), process.first_step_id)
            # step_task(str(process.id), process.first_step_id)
