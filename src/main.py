# import functools
# import asyncio
# from typing import Coroutine
# import typing
# from typing import List, Optional, Union
# import inspect

# from datetime import datetime
# from enum import Enum

# from fastapi_users import fastapi_users, FastAPIUsers, models, schemas, exceptions
# from pydantic import BaseModel, Field

# from fastapi import FastAPI, Request, status, Depends
# from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import ValidationException
# from fastapi.responses import JSONResponse

# from auth.auth import auth_backend
# from auth.database import User
# from auth.manager import get_user_manager
# from auth.schemas import UserRead, UserCreate


# # def answer_dec(func):
# #     @functools.wraps(func)
# #     async def wrapper(*args, **kwargs):
# #         print(type(func))
# #         try:
# #             if inspect.iscoroutinefunction(func):
# #                 result = await func(*args, **kwargs)
# #             else:
# #                 result = func(*args, **kwargs)
# #             answer ={"status": 200,
# #                         "Errors": False,
# #                         "discription": None,
# #                         "data": result}
# #         except Exception as e:
# #             print(e)
# #             answer = {"status": 200,
# #                       "Errors": True,
# #                       "discription": f"{e}",
# #                       "data": None}
# #         return answer
# #     return wrapper


# app = FastAPI()

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )


# current_user = fastapi_users.current_user()

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"


# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonym"

# users = [{"id": 1, "Name": "Alex", "role":"q"},
#          {"id": 2,"Name": "John", "role":"w"},
#          {"id": 3,"Name": "Michael", "role": [{"name": "god", "appointment_date": datetime.utcnow()}]}] #"appointment_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

# class RoleName(Enum):
#     god = "god"
#     you = "you"

# class Role(BaseModel):
#     name: str
#     appointment_date: datetime

# class User(BaseModel):
#     id: int
#     Name: str
#     role: typing.List[Role]

# @app.get("/user/{user_id}", response_model=typing.List[User])
# # @answer_dec
# async def get_user(user_id: int):
#     return [user for user in users if user.get("id") == user_id]


# @app.post("/user/{user_id}")
# @answer_dec
# async def change_name(user_id: int, new_name: str):
#     user = [user for user in users if user.get("id")==user_id][0]
#     user["Name"] = new_name
#     return {"status": 200,
#             "Errors": False,
#             "discription": None,
#             "data": user}
    
# trades = [
#     {"id": 1, "cur": "rub", "value": 123},
#     {"id": 2, "cur": "BTC", "value": 666}
# ]

# class Trade(BaseModel):
#     id: int
#     cur: str = Field(max_length=5)
#     value: float =Field(ge=0)

# @app.post("/trades")
# @answer_dec
# def add_trades(new_trades: typing.List[Trade]):
#     trades.extend(new_trades)
#     return trades
# # @status_code_dec
# # async def myew():
# #     await asyncio.sleep(3)
# #     return "!!!!!!!!!"
    

# # async def main():
# #     print(await myew())


# # if __name__=="__main__":
# #     asyncio.run(main())


import inspect
import functools
from fastapi import Depends, FastAPI

from auth.base_config import current_user
from auth.base_config import auth_backend, fastapi_users
from auth.models import User
from auth.schemas import UserRead, UserCreate

# from operations.router import router as router_operation

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# app.include_router(router_operation)

def answer_dec(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print(type(func))
        try:
            if inspect.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            answer ={"status": 200,
                        "Errors": False,
                        "discription": None,
                        "data": result}
        except Exception as e:
            print(e)
            answer = {"status": 200,
                      "Errors": True,
                      "discription": f"{e}",
                      "data": None}
        return answer
    return wrapper

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"