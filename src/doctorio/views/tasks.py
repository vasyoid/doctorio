
from fastapi import APIRouter
from pydantic import BaseModel

from ..models.customers import Customer
from ..models.tasks import Task, DoneTask

router = APIRouter()


class TaskModel(BaseModel):
    hospital: str
    address: str
    name: str
    surname: str


@router.post("/tasks/add")
async def add_task(task: TaskModel):
    rv = await Task.create(hospital=task.hospital, address=task.address, name=task.name, surname=task.surname)
    return rv


@router.get("/tasks/result/{uid}")
async def get_task_result(uid: int):
    rv = await DoneTask.query.where(DoneTask.id == uid).gino.all()
    yes = 0
    no = 0
    for task in rv:
        if task.verdict:
            yes += 1
        else:
            no += 1
    if yes + no < 3:
        return "not enough verdicts"
    else:
        return yes > no


class SubmitModel(BaseModel):
    task: int
    customer: int
    verdict: bool


@router.post("/tasks/submit")
async def submit_verdict(submit: SubmitModel):
    rv = await DoneTask.create(id=submit.task, customer=submit.customer, verdict=submit.verdict)
    c = await Customer.get_or_404(submit.customer)
    await c.update(bonuses=c.bonuses + 9).apply()
    return rv


def init_app(app):
    app.include_router(router)
