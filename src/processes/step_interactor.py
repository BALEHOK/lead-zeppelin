from src.processes.models import ProccessStep, StepType


class StepInteractor:
    @staticmethod
    def execute_step(step: ProccessStep):
        if step.type == StepType.message.name:
            print(step.message)
