from fastapi import APIRouter, Request

from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/web", tags=["Фронтенд"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/auth")
async def get_registration_html(request: Request):
    return templates.TemplateResponse(name="auth.html", context={"request": request})



@router.get("/index")
async def get_index_html(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


@router.get("/profile")
async def get_profile_html(request: Request):
    return templates.TemplateResponse(name="profile.html", context={"request": request})


@router.get("/support")
async def get_support_html(request: Request):
    return templates.TemplateResponse(name="support.html", context={"request": request})


@router.get("/ticket1")
async def get_ticket1_html(request: Request):
    return templates.TemplateResponse(name="ticket1.html", context={"request": request})


@router.get("/ticket2")
async def get_ticket2_html(request: Request):
    return templates.TemplateResponse(name="ticket2.html", context={"request": request})


@router.get("/ticket3")
async def get_ticket3_html(request: Request):
    return templates.TemplateResponse(name="ticket3.html", context={"request": request})


@router.get("/ticket4")
async def get_ticket4_html(request: Request):
    return templates.TemplateResponse(name="ticket4.html", context={"request": request})


@router.get("/ticket5")
async def get_ticket5_html(request: Request):
    return templates.TemplateResponse(name="ticket5.html", context={"request": request})


@router.get("/ticket6")
async def get_ticket6_html(request: Request):
    return templates.TemplateResponse(name="ticket6.html", context={"request": request})


@router.get("/ticket7")
async def get_ticket7_html(request: Request):
    return templates.TemplateResponse(name="ticket7.html", context={"request": request})


@router.get("/ticket8")
async def get_ticket8_html(request: Request):
    return templates.TemplateResponse(name="ticket8.html", context={"request": request})


@router.get("/ticket9")
async def get_ticket9_html(request: Request):
    return templates.TemplateResponse(name="ticket9.html", context={"request": request})