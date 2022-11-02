from fastapi import FastAPI


print('Hello')


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

print('End')



















