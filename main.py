import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.sample import router as sample_router
from app.api.auth import router as auth_router
from app.api.roles import router as role_router
from app.api.planes import router as planes_router
from app.api.air_companies import router as air_companies_router
from app.api.cities import router as cities_router
from app.api.web import router as web_router

app = FastAPI(title="Система бронирования авиабилетов", version="1.0.0")

app.mount("/static", StaticFiles(directory="app/static"), "static")
app.include_router(sample_router)
app.include_router(auth_router)
app.include_router(role_router)
app.include_router(planes_router)
app.include_router(air_companies_router)
app.include_router(cities_router)
app.include_router(web_router)

if __name__ == "__main__":
    uvicorn.run(app=app)