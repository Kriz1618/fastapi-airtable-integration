import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from src.routes import router

reload = os.environ.get('ENV', 'production') == 'local'
port = int(os.environ.get('PORT', '8000'))
app = FastAPI()

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("main:app", port=port, reload=reload)
