from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CL_USER = os.getenv("CL_USER")
CL_PASS = os.getenv("CL_PASS")

LOGIN_URL = "https://carelink.minimed.eu/patient/sso/login"
DATA_URL  = "https://carelink.minimed.eu/patient/connect/data?cp_serial=0"

session = requests.Session()
app = FastAPI()

def carelink_login():
    payload = {
        "login": CL_USER,
        "password": CL_PASS
    }
    session.post(LOGIN_URL, data=payload)

@app.get("/glucose")
def get_glucose():
    try:
        carelink_login()
        r = session.get(DATA_URL)
        data = r.json()

        last = data["lastSG"]
        return {
            "glucose": last["sg"],
            "trend": last["trend"],
            "timestamp": last["datetime"]
        }
    except Exception as e:
        return {"error": str(e)}
