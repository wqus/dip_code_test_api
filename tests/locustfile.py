from locust import HttpUser, task, between
import random


class APIUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 2)

    def on_start(self):

        # создание user
        user_resp = self.client.post(
            "/users",
            json={"name": f"test_user_{random.randint(1, 99999)}"}
        )

        self.user_id = user_resp.json()["id"]

        # создание devices
        device_resp = self.client.post(
            "/devices",
            json={
                "user_id": self.user_id,
                "name": f"device_{random.randint(1, 99999)}"
            }
        )

        self.device_id = device_resp.json()["id"]

    @task(5)
    def create_stats(self):
        self.client.post(
            "/stats",
            json={
                "device_id": self.device_id,
                "x": random.uniform(0, 100),
                "y": random.uniform(0, 100),
                "z": random.uniform(0, 100),
            }
        )

    @task(3)
    def get_stats(self):
        self.client.get(f"/stats/{self.device_id}")
    @task(2)
    def device_analytics(self):
        self.client.get(f"/analytics/device/{self.device_id}")

    @task(2)
    def user_analytics(self):
        self.client.get(f"/analytics/user/{self.user_id}")

    @task(1)
    def user_devices_analytics(self):
        self.client.get(f"/analytics/user/{self.user_id}/devices")