from src.processes.models import ProcessStep, StepType


class StepInteractor:
    @staticmethod
    def execute_step(step: ProcessStep):
        if step.type == StepType.message.name:
            print(step.message)
