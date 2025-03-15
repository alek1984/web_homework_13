from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import FastAPI, Depends
from fastapi.routing import APIRouter

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

router = APIRouter()

@router.post("/contacts", dependencies=[Depends(limiter.limit("5/minute"))])
async def create_contact():
    return {"message": "Контакт створено"}

