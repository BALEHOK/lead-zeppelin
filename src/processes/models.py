import uuid
from enum import Enum, auto

from mongoengine import Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ListField, UUIDField, \
    IntField, DateTimeField


class StepType(Enum):
    delay = auto()
    wait_until = auto()
    message = auto()


class ProcessStep(EmbeddedDocument):
    meta = {'allow_inheritance': True}

    step_id = UUIDField(default=uuid.uuid4)
    name = StringField()
    description = StringField()
    prev_step_id = UUIDField()


class ProcessStepDelay(ProcessStep):
    type = StringField(default=StepType.delay.name)
    delay = IntField()


class ProcessStepMessage(ProcessStep):
    type = StringField(default=StepType.message.name)
    message = StringField()


class ProcessStepWaitUntil(ProcessStep):
    type = StringField(default=StepType.wait_until.name)
    when = DateTimeField()


class Process(Document):
    bound_entity_id = StringField(required=True)
    name = StringField()
    description = StringField()
    first_step_id = UUIDField()
    steps = ListField(EmbeddedDocumentField(ProcessStep))
