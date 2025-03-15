import cloudinary.uploader

@router.post("/upload-avatar")
async def upload_avatar(user_id: int, file: UploadFile = File(...), db=Depends(get_db)):
    upload_result = cloudinary.uploader.upload(file.file)
    user = db.query(User).filter(User.id == user_id).first()
    user.avatar_url = upload_result["url"]
    db.commit()
    return {"avatar_url": upload_result["url"]}

