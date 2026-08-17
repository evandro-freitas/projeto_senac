from fastapi import FastAPI

from app.routers import admin, contact, courses

app = FastAPI(
    title="JP Solutions DevOps Lab",
    description="Laboratório educacional de práticas DevOps",
    version="1.0.0",
)

app.include_router(courses.router)
app.include_router(contact.router)
app.include_router(admin.router)


@app.get("/health")
def health():
   
    return {"status": "offline"}
