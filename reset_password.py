@router.post("/reset-password")
async def reset_password(email: str, db=Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user:
        token = str(uuid.uuid4())
        user.reset_token = token
        db.commit()
        await send_reset_email(email, token)
    return {"message": "Перевірте email для зміни пароля"}
