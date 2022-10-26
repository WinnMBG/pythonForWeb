from fastapi import FastAPI
from pydantic import BaseModel

class Infos(BaseModel):
	name: str
	lastname: str
	age: int
	location: str
	
app = FastAPI()

fake_db = [{"first":1},{"second":2},{"third":3},{"forth":4},{"fifth":5}]

@app.get("/")
async def root():
	return {"message":"hello world!"}
	
@app.get("/ids/{id}")
async def getIds(id: int):
	return {"identifiant": id}
	
@app.get("/numbers/{id}")
async def getNumbers(id: int,skip : int=0, limit: int=2):
	if(id <= 0):
		return {"message" : "Le nombre renvoyé est trop négatif"}
	else:
		return fake_db[id-1]

@app.post("/postinfos")
async def postInfos(infos: Infos):
	if(infos.age <= 18):
		return {"message": "Vous êtes mineur, enregistrement impossible"}	
	fake_db.append(infos)
	return fake_db

