from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)
    # a = 0
    # b = 0
    # c = 0 

    @task
    def test_index(self):
        response = self.client.get('/')
        message = response.json()['message']
        # print(message)
        # if message == 'This is server A':
        #     self.a += 1
        # elif message == 'This is server B':
        #     self.b += 1
        # elif message == 'This is server C':
        #     self.c += 1
        
        # print(f'A: {self.a}, B: {self.b}, C: {self.c}')
    
    @task
    def test_fast(self):
        self.client.get('/fast')
    
    @task
    def test_slow(self):
        self.client.get('/slow')
    
    @task
    def test_slow(self):
        self.client.get('/all')

    @task
    def test_get_id(self):
        response = self.client.get('/get/[ID]')
        message = response.json()['message']
        # if message == 'A':
        #     self.a += 1
        # elif message == 'B':
        #     self.b += 1
        # elif message == 'C':
        #     self.c += 1
        
        # print(f'A: {self.a}, B: {self.b}, C: {self.c}')
