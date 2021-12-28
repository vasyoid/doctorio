from fastapi import APIRouter
from pydantic import BaseModel

from ..models.customers import Customer
from ..models.feedback import *

router = APIRouter()


class FeedbackModel(BaseModel):
    customer: int
    doctor: int
    rating: int
    comment: str


@router.post("/feedback")
async def add_feedback(feedback: FeedbackModel):
    c = await Customer.get_or_404(feedback.customer)
    await c.update(bonuses=c.bonuses + 15).apply()
    await Feedback.create(doctor=feedback.doctor, rating=feedback.rating, comment=feedback.comment)
    return "ok"


@router.get("/feedback/{uid}")
async def collect_feedback(uid: int):
    rv = await Feedback.query.where(Feedback.doctor == uid).gino.all()
    result = {"rating": 0, "comments": []}
    for feedback in rv:
        result["rating"] += feedback.rating
        result["comments"].append(feedback.comment)
    result["rating"] /= len(rv)
    return result


def init_app(app):
    app.include_router(router)
