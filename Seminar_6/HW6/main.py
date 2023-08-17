import uvicorn
from db import *
from fastapi import FastAPI, Request, HTTPException
import items_router
import users_router
# import order_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(users_router.router, tags=['Users'])
app.include_router(items_router.router, tags=['Item'])
# app.include_router(order_router.router, tags=['Order'])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        # host="127.0.0.1",
        # port=8000,
        reload=True
    )
