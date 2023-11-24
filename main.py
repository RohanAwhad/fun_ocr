import pytesseract

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)
    return {"filename": file.filename, "text": text}
