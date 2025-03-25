from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def profile():
    return {"username": "demo_user", "2fa_enabled": True}

@router.post("/enable_mfa")
def enable_mfa():
    return {"status": "MFA enabled"}

@router.post("/ip_whitelist")
def whitelist_ip(ip: str):
    return {"status": f"IP {ip} whitelisted"}
