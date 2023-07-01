from fastapi import FastAPI,  Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="build")



_response="Hello World"




# Serves static react pages
@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# serves api call to the chatgpt
@app.get("/api")
async def root():
    return {"message": _response}