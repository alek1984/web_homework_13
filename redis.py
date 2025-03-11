import redis

redis_client = redis.Redis(host="redis", port=6379, db=0)

def cache_user(user_id, user_data):
    redis_client.setex(f"user:{user_id}", 3600, json.dumps(user_data))

def get_cached_user(user_id):
    data = redis_client.get(f"user:{user_id}")
    return json.loads(data) if data else None
