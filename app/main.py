from fastapi import FastAPI
from app.api.routes.stats import router as stats_router
from app.api.routes.analytics import router as analytics_router
from app.api.routes.users import router as users_router
from app.api.routes.devices import router as devices_router

app = FastAPI(title='dip code test')

app.include_router(stats_router)
app.include_router(analytics_router)
app.include_router(users_router)
app.include_router(devices_router)


@app.get("/")
async def root():
    return {
        "status": "ok",
    }
