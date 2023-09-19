from fastapi import FastAPI, Response
import uvicorn

from resources.students import StudentsResource

app = FastAPI()

students_resource = StudentsResource()

# RITWIK GOEL 
# rg3546- Columbia University

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Awesome cloud developer (RITWIK) says hello {name}"}


@app.get("/hello_text/{name}")
async def say_hello_text(name: str):
    the_message = f"Awesome cloud developer dff9 says Hello {name}"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/students")
async def get_students():
    result = students_resource.get_students()
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
