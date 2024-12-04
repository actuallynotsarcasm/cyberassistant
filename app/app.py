from fastapi import FastAPI
from asyncio import Semaphore
from contextlib import asynccontextmanager
from llama_cpp import Llama
import uvicorn
import app

from router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = Llama.from_pretrained(
        repo_id="bartowski/Llama-3.2-1B-Instruct-GGUF",
        filename="Llama-3.2-1B-Instruct-Q4_K_S.gguf",
        n_ctx=1024
    )
    app.state.desc_sem = Semaphore()
    app.state.model_sem = Semaphore()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)