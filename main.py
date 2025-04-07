from fastapi import FastAPI
import auth, users, trades
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="QuantumTrade API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to your frontend domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(trades.router, prefix="/trades")

@app.get("/")
def root():
    return {"message": "QuantumTrade API is running"}
