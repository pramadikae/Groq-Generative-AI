from locust import HttpUser, task, between
import random
from src.questions import get_random_question

class AIServiceUser(HttpUser):
    # Waktu tunggu antar request (1-3 detik)
    wait_time = between(1, 3)

    @task
    def ask_ai(self):
        # Pilih pertanyaan random dari list
        question = get_random_question()
        payload = {
            "messages": [
                {"role": "user", "content": question}
            ]
        }
        # Kirim POST ke endpoint /chat
        with self.client.post("/chat", json=payload, stream=True, catch_response=True) as response:
            if response.status_code == 200:
                response.success()  # Request berhasil
            else:
                response.failure(f"Failed: {response.status_code}")  # Gagal
