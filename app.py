from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/process-multipart")
async def process_multipart(
    title: str = Form(...),
    content_html: str = Form(...),
    image: UploadFile = File(...)
):
    content = await image.read()
    return JSONResponse({
        "ok": True,
        "title": title,
        "html_len": len(content_html),
        "image_name": image.filename,
        "content_type": image.content_type,
        "image_size": len(content)
    })
