import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src.api.books.routes import router as books_router
from src.api.users.routes import router as users_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


api_v1_router = APIRouter(prefix='/api/v1')
api_v1_router.include_router(users_router)
api_v1_router.include_router(books_router)
app.include_router(api_v1_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
