from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "pnl": 812.25,
        "active_trades": 4,
        "ai_mode": True
    }

@router.post("/toggle_ai")
def toggle_ai():
    return {"status": "AI trading toggled"}

@router.get("/logs")
def logs():
    return {
        "logs": [
            {"symbol": "BTC/USDT", "action": "BUY", "profit": 25.4},
            {"symbol": "ETH/USDT", "action": "SELL", "profit": -12.1}
        ]
    }
