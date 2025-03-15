import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_user(user_id, user_data):
    redis_client.set(f"user:{user_id}", user_data, ex=3600)

def get_cached_user(user_id):
    return redis_client.get(f"user:{user_id}")

