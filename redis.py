import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_user(user_id, user_data):
    redis_client.set(f"user:{user_id}", user_data, ex=3600)

def get_cached_user(user_id):
    return redis_client.get(f"user:{user_id}")
@router.get("/user/{user_id}")
async def get_user(user_id: int, db=Depends(get_db)):
    cached_user = get_cached_user(user_id)
    if cached_user:
        return cached_user

    user = db.query(User).filter(User.id == user_id).first()
    if user:
        cache_user(user_id, user)
        return user

    raise HTTPException(status_code=404, detail="User not found")

