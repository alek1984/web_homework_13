import cloudinary.uploader

def upload_avatar(file):
    result = cloudinary.uploader.upload(file.file)
    return result["url"]
