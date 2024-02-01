from fastapi import FastAPI
import uvicorn
from fastapi_cdn_host import monkey_patch_for_docs_ui

app = FastAPI()
monkey_patch_for_docs_ui(app)

@app.get("/get")
def get_test():
    return {"method":"get method"}

if __name__ =="__main__":
    uvicorn.run(app='l1:app', port=8000 , reload=True , workers=3)