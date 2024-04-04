from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from genai_api.api.DeepAI import speech_to_text
from genai_api.prompts.prompts import get_prompt
from genai_api.models.generative_llm import llm

app = FastAPI()
templates = Jinja2Templates(directory="genai_api/templates/")


class Item(BaseModel):
    input_audio: str


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload_file")
async def create_item(input_audio: UploadFile = File(...)):
    content = await input_audio.read()
    transcript = speech_to_text(content)
    prompt = get_prompt(transcript)
    genai_func_call = llm(prompt)
    cleaned_text = genai_func_call.replace("\n", "")
    return cleaned_text
