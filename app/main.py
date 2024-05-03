from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/next-fibonacci")
def read_item(number: int):
    return next_fibonacci(number)

def next_fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if n in fib:
        return fib[len(fib)-1] + fib[len(fib)-2]
    else:
        return "Not a fibonacci number."
