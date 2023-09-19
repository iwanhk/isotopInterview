import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    host = "http://47.109.33.239:8001"  # 访问的站点，最后不要加斜杠
    # wait_time = between(1, 2)
    min_wait = 1000
    max_wait = 5000

    @task
    def index_page(self):
        self.client.get("/nft")

    def on_start(self):
        pass
