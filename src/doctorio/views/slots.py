import time

from fastapi import APIRouter
from pydantic import BaseModel

from ..models.customers import Customer
from ..models.slots import FreeSlot, BusySlot

router = APIRouter()


class SlotModel(BaseModel):
    doctor: int
    timestamp: int


@router.post("/slots/add")
async def add_slot(slot: SlotModel):
    await FreeSlot.create(doctor=slot.doctor, timestamp=slot.timestamp)
    return "ok"


@router.delete("/slots/delete/{doctor}/{timestamp}")
async def delete_slot(doctor: int, timestamp: int):
    rv = await FreeSlot.get_or_404((doctor, timestamp))
    await rv.delete()
    return "ok"


@router.get("/slots/available/{doctor}")
async def list_slots(doctor: int):
    rv = await FreeSlot.query.where(FreeSlot.doctor == doctor).gino.all()
    return [slot.timestamp for slot in rv]


class BookModel(BaseModel):
    doctor: int
    timestamp: int
    customer: int


@router.post("/slots/book")
async def book_slot(book: BookModel):
    slot = await FreeSlot.get_or_404((book.doctor, book.timestamp))
    await slot.delete()
    await BusySlot.create(doctor=book.doctor, timestamp=book.timestamp, customer=book.customer)
    return "ok"


MIN_CANCEL_TIME = 24 * 60 * 60


@router.delete("/slots/book")
async def cancel_booking(book: BookModel):
    result = "ok"
    slot = await BusySlot.get_or_404((book.doctor, book.timestamp))
    if book.timestamp - time.time() < MIN_CANCEL_TIME:
        c = await Customer.get_or_404(book.customer)
        await c.update(misses=c.misses + 15).apply()
        if c.misses >= 5:
            result = "warning"
            await c.update(bonuses=c.bonuses - 10).apply()
            if c.bonuses < 0:
                await c.delete()
                return "user deleted"
    await slot.delete()
    await BusySlot.create(doctor=book.doctor, timestamp=book.timestamp, customer=book.customer)
    return result


def init_app(app):
    app.include_router(router)
