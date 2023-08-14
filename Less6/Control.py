from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of theitem"), q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id":"Eggs"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Spam"}, {"item_id":"Eggs"}]}
    if q:
        results.update({"q": q})
    return results

