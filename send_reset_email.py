async def send_reset_email(email: str, token: str):
    message = MessageSchema(
        subject="Скидання пароля",
        recipients=[email],
        body=f"Перейдіть за посиланням для зміни пароля: http://127.0.0.1:8000/reset/{token}",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
