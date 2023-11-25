from django.core.cache import cache

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Increment the request count in the cache
        cache_key = 'request_count'
        request_count = cache.get(cache_key, 0)
        cache.set(cache_key, request_count + 1)

        response = self.get_response(request)
        return response
