# import uvicorn
# from db import *
# from fastapi import FastAPI, Request, HTTPException
# import r_posts
# import users_1
#
# app = FastAPI()
#
#
# @app.on_event("startup")
# async def startup():
#     await db.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()
#
#
# app.include_router(users_1.router, tags=['users'])
# app.include_router(r_posts.router, tags=['posts'])
#
# if __name__ == '__main__':
#     uvicorn.run(
#         "main:app",
#         # host="127.0.0.1",
#         # port=8000,
#         reload=True
#     )
