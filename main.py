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
    allow_origins=["https://tugui142.github.io"], # URL exacta de tu frontend sin barra "/" al final
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
        
        # 3. Abrir la hoja de cálculo por su nombre
        sheet = client.open("eafit-pedidos-mvp").sheet1
        
        # 4. Insertar la nueva fila con los datos del pedido
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fila = [order.id, timestamp, order.items, order.time, order.total, order.status]
        sheet.append_row(fila)
        
        return {"status": "success", "message": f"Pedido {order.id} registrado correctamente en Sheets"}
        
    except Exception as e:
        print(f"Error interno: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pedidos")
async def get_orders():
    # 1. Recuperar el JSON de la cuenta de servicio
    creds_json = os.environ.get("GOOGLE_CREDENTIALS")
    if not creds_json:
        raise HTTPException(status_code=500, detail="Faltan credenciales")
    
    try:
        # 2. Autenticación
        creds_dict = json.loads(creds_json)
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        client = gspread.authorize(creds)
        
        # 3. Leer la hoja de cálculo
        sheet = client.open("eafit-pedidos-mvp").sheet1
        valores = sheet.get_all_values()
        
        # 4. Estructurar los datos para enviarlos a la página web
        pedidos = []
        for fila in valores:
            # Filtra solo las filas que tengan un ID numérico (ignorando la primera fila de encabezados)
            if len(fila) >= 6 and str(fila[0]).isdigit():
                pedidos.append({
                    "id": int(fila[0]),
                    "items": fila[2],
                    "time": fila[3],
                    "status": fila[5]
                })
        return pedidos
        
    except Exception as e:
        print(f"Error interno: {e}")
        raise HTTPException(status_code=500, detail=str(e))
