"""Main API routes"""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data import calculate_car, CarForm
from ai import generate_msg

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def get_index(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/form/', response_class=HTMLResponse)
def get_form(request: Request):
    """Form page"""
    return templates.TemplateResponse("form.html", {"request": request})

@app.post('/form/', response_class=HTMLResponse)
def get_results(request: Request, type: str = Form(None), engine: str = Form(None), price: int = Form(2000000), seats: int = Form(None), uses: list = Form(...), allterrain: bool = Form(False), comment: str = Form("")):
    """Results page"""
    form = CarForm(type=type, engine=engine, price=price, seats=seats, uses=uses, allterrain=allterrain)
    car = calculate_car(form)
    img = car["name"].lower().replace(' ', '_').replace('-', '_')
    msg = generate_msg(car, comment)
    li = []
    if car["price"] < price:
        li.append("It's within your budget")
    if car["type"] == type:
        if type == "sports":
            type += " car"
        li.append(f"It is a {type}")
    if car["engine"] == engine:
        li.append(f"It has a {engine} engine")
    if car["seats"] == seats:
        li.append(f"It has {str(seats)} seats")
    if car["allterrain"] and allterrain:
        li.append("It can go all terrain")
    uses_desired = [use for use in uses if use in car["uses"]]
    if len(uses_desired) > 0:
        li.append("Perfect for: " + ", ".join(uses_desired))
    ai_title = "Can you picture this?"
    if comment == "": 
        ai_title = "Is this you?"

    return templates.TemplateResponse("results.html", {"request": request, "car": car, "img": img, "li": li, "msg": msg, "ai_title": ai_title})
