
from fastapi import APIRouter
from pydantic import BaseModel

from ..models.customers import Customer

router = APIRouter()


class CustomerModel(BaseModel):
    name: str
    surname: str


@router.post("/customer")
async def add_customer(customer: CustomerModel):
    rv = await Customer.create(name=customer.name, surname=customer.surname)
    return rv.to_dict()


@router.get("/customer/{uid}")
async def get_customer(uid: int):
    rv = await Customer.get_or_404(uid)
    return rv.to_dict()


@router.delete("/customer/{uid}")
async def delete_customer(uid: int):
    rv = await Customer.get_or_404(uid)
    await rv.delete()
    return dict(id=uid)


def init_app(app):
    app.include_router(router)
