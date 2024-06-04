import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def update_endpoint(endpoint_id, metadata):
    r.hmset(endpoint_id, metadata)

def get_endpoint_metadata(endpoint_id):
    return r.hgetall(endpoint_id)
