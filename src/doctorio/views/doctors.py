from typing import List

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import and_

from ..models.doctors import *

router = APIRouter()


class HospitalModel(BaseModel):
    name: str
    address: str


@router.post("/hospital")
async def add_hospital(hospital: HospitalModel):
    rv = await Hospital.create(name=hospital.name, address=hospital.address)
    return rv.to_dict()


@router.get("/hospital/{uid}")
async def get_hospital(uid: int):
    rv = await Hospital.get_or_404(uid)
    return rv.to_dict()


@router.delete("/hospital/{uid}")
async def delete_hospital(uid: int):
    rv = await Hospital.get_or_404(uid)
    await rv.delete()
    return dict(id=uid)


class DoctorModel(BaseModel):
    hospital: int
    name: str
    surname: str
    cost: int
    competences: List[str]


@router.post("/doctor")
async def add_doctor(doctor: DoctorModel):
    rv = await Doctor.create(hospital=doctor.hospital, name=doctor.name, surname=doctor.surname, cost=doctor.cost)
    for competence in doctor.competences:
        await Competence.create(doctor=rv.id, title=competence)
    return dict(id=rv.id)


@router.get("/doctor/{uid}")
async def get_doctor(uid: int):
    rv = await Doctor.get_or_404(uid)
    rv_dict = rv.to_dict()
    rv_dict["competences"] = []
    for competence in await Competence.query.where(Competence.doctor == uid).gino.all():
        rv_dict["competences"].append(competence.title)
    return rv_dict


@router.delete("/doctor/{uid}")
async def delete_doctor(uid: int):
    rv = await Doctor.get_or_404(uid)
    await rv.delete()
    return dict(id=uid)


@router.get("/doctors/find")
async def find_doctor(cost: int, title: str = None):
    d_filter = Doctor.cost <= cost
    if title:
        d_filter = and_(d_filter, Competence.title == title)
    rv = await Doctor.load(competence=Competence.on(Doctor.id == Competence.doctor))\
        .where(d_filter)\
        .gino.all()
    return set([doctor.id for doctor in rv])


def init_app(app):
    app.include_router(router)
