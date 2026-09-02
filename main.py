import os
import json
import gspread
from google.oauth2.service_account import Credentials
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Configuración CORS: Permite que tu GitHub Pages se comunique con este servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Por seguridad, puedes cambiar el "*" por la URL de tu GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estructura de datos que enviará tu frontend
class Order(BaseModel):
    id: int
    items: str
    time: str
    total: int
    status: str

@app.post("/nuevo-pedido")
async def create_order(order: Order):
    # 1. Recuperar el JSON de la cuenta de servicio desde Render
    creds_json = os.environ.get("GOOGLE_CREDENTIALS")
    if not creds_json:
        raise HTTPException(status_code=500, detail="Faltan las credenciales de Google")
    
    try:
        # 2. Autenticación con la API de Google Sheets
        creds_dict = json.loads(creds_json)
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        client = gspread.authorize(creds)
        
        # 3. Abrir la hoja de cálculo por su nombre (Asegúrate de que este nombre sea exacto)
        # IMPORTANTE: Debes compartir tu archivo de Google Sheets con el correo de la cuenta de servicio
        sheet = client.open("eafit-pedidos-mvp").sheet1
        
        # 4. Insertar la nueva fila con los datos del pedido
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fila = [order.id, timestamp, order.items, order.time, order.total, order.status]
        sheet.append_row(fila)
        
        return {"status": "success", "message": f"Pedido {order.id} registrado correctamente en Sheets"}
        
    except Exception as e:
        print(f"Error interno: {e}")
        raise HTTPException(status_code=500, detail=str(e))
