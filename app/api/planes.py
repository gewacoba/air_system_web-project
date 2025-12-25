from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.schemes.planes import SPlaneAdd, SPlaneGet
from app.services.planes import PlaneService

router = APIRouter(prefix="/planes", tags=["Управление самолетами"])


@router.post("/", summary="Создание нового самолета")
async def create_new_plane(
    plane_data: SPlaneAdd,
    db: DBDep,
) -> dict[str, str]:
    await PlaneService(db).add_plane(plane_data)
    return {"status": "OK"}


@router.get("/", summary="Получение списка самолетов")
async def get_all_planes(
    db: DBDep,
) -> list[SPlaneGet]:
    planes = await PlaneService(db).get_all_planes()
    return planes


@router.get("/{id}", summary="Получение конкретного самолета")
async def get_plane(
    db: DBDep,
    id: int,
) -> SPlaneGet | None:
    plane = await PlaneService(db).get_plane(id)
    return plane


@router.put("/{id}", summary="Изменение конкретного самолета")
async def update_plane(
    db: DBDep,
    plane_data: SPlaneAdd,
    id: int,
) -> dict[str, str]:
    await PlaneService(db).update_plane(id, plane_data)
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление конкретного самолета")
async def delete_plane(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    await PlaneService(db).delete_plane(id)
    return {"status": "OK"}