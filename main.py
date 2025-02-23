import uvicorn
from fastapi import FastAPI, APIRouter
from src.routes import router


app = FastAPI()
api_v1_router = APIRouter(prefix='/api/v1')
api_v1_router.include_router(router)
app.include_router(api_v1_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
