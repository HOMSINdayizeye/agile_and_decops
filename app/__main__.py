import uvicorn

from app import create_app

if __name__ == "__main__":
    # Bind to 127.0.0.1 so the printed URL is directly browseable.
    # (0.0.0.0 binds all interfaces but is NOT a valid browser address.)
    uvicorn.run(create_app(), host="127.0.0.1", port=5000)
