import uvicorn

from fastapi import FastAPI

from routers.router import router as router_files

app = FastAPI(title="File Cloud", version="93", description="File Cloud is a service where you can check, upload, "
                                                            "download and delete any files what do you want.")
app.include_router(router_files)  # connect routers

if __name__ == '__main__':  # It's a useless code for someone (you can write it in a terminal 'uvicorn main:app
    # --reload'. It's the same)
    uvicorn.run('main:app', reload=True)
