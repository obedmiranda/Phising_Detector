from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importar las rutas (más adelante tendrás /analyze aquí)
# from app.routes import analyze
from app.routes import analyze
app = FastAPI(title="Phishing Detector")

# Servir los archivos estáticos (CSS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar las plantillas HTML (Jinja2)
templates = Jinja2Templates(directory="templates")

# Registrar routers adicionales
app.include_router(analyze.router, prefix="/api", tags=["Phishing Analysis"])

# Ruta raíz: renderizar el index.html
@app.get("/", response_class=HTMLResponse)
async def render_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
