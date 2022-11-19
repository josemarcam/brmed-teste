

def requests_get_mock(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    
    return MockResponse({"date":"2022-11-14","rates":{"EUR":1,"USD":1.0366,"JPY":145.12,"BGN":1.9558,"CZK":24.351,"DKK":7.4385,"GBP":0.87063,"HUF":407.41,"PLN":4.7033}}, 200)


def cache_mock(*args, **kwargs):
    class MockCache:
        def __init__(self, *args, **kwargs):...

        def has_key(self):
            return False
        
        def get(self):
            return {"2022-11-14":{"EUR":1,"USD":1.0366,"JPY":145.12,"BGN":1.9558,"CZK":24.351,"DKK":7.4385,"GBP":0.87063,"HUF":407.41,"PLN":4.7033}}

        def set(self):
            return True
    

    return MockCache()