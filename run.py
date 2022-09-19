import uvicorn
from src.common.config.settings import settings


def start_app():
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )


if __name__ == "__main__":
    start_app()
