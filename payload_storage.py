import redis

r = redis.Redis(host='localhost', port=6379, db=1)

def save_payload(key, payload):
    r.set(key, payload)

def get_payload(key):
    return r.get(key)
