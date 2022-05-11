import uvicorn
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from predict import Prediction

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
def upload(request: Request):
    return templates.TemplateResponse("upload-form.html", {"request": request})


@app.post('/', response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    prediction = Prediction()
    image = prediction.read_image(await file.read())
    preprocessed_image = prediction.preprocess(image)
    predicted_label = prediction.predict(preprocessed_image)
    return templates.TemplateResponse("upload-form.html", {"request": request, "result": predicted_label})

if __name__ == "__main__":
    uvicorn.run(app)
