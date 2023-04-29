from fastapi import FastAPI, Request, File, HTTPException, UploadFile
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Body

app = FastAPI()
# Templates is for working with html files in /templates forder
templates = Jinja2Templates(directory="templates")
# We need to mount a folder for our files (images, audio, videos), staticFiles will do it
app.mount("/static", StaticFiles(directory="static"), name="static")
# The root route will send to the user the html file
