from locust import HttpUser, task, between


class TestCase01(HttpUser):
    wait_time = between(1, 3)  # 每个请求之间等待 1~3 秒

    @task
    def get_public_get_test(self):
        self.client.get("/public/test")

    @task
    def get_public_post_test(self):
        self.client.post("/public/test", json={"msg": "1234"})


# locust -f testcase01.py --host=http://localhost:9882 --users 100 --spawn-rate 10 --headless --run-time 1m --csv report.csv
# locust -f testcase01.py --host=http://localhost:9882 --users 100 --spawn-rate 10 --headless --run-time 1m --html report.html

# --users	模拟用户数量
# --spawn-rate	每秒启动多少个用户
# --headless	无 UI 模式，适合自动化测试
# --run-time	总运行时间，例如 2m, 30s
# --csv	输出 CSV 格式的测试报告
