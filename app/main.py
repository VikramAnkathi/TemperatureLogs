from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn, csv

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="templates")

fake_users = {
    "admin": "password",
}

@app.get("/", response_class = HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("hello.html", {"request": request})

@app.get("/login/", response_class = HTMLResponse)
async def login_form(request: Request):
    return template.TemplateResponse("login.html", {"request": request})

@app.post("/login/", response_class = HTMLResponse)
async def login(request: Request, name:str=Form(...), password:str=Form(...)):
    if name in fake_users and fake_users['admin'] == password:
        return template.TemplateResponse("loginsuccessful.html", {"request": request, "name": name})
    else:
        return template.TemplateResponse("login.html", {"request": request , "error_message": "Unverified UserName or Password"})

@app.post("/save/", response_class = HTMLResponse)
async def save(request: Request, num:float=Form(...)):
    header_list = ["Temp",]
    if num:
        with open('/Users/vikramankathi/Downloads/temperature.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([num])
        return template.TemplateResponse("loginsuccessful.html", {"request": request})
