# locust -f testcase01.py --host=http://localhost:9882 --users 100 --spawn-rate 10 --headless --run-time 1m --csv report.csv

# locust -f testcase01.py --host=http://localhost:9882 --users 100 --spawn-rate 10 --headless --run-time 1m --html report.html


## 📌 常用参数详解

| 参数                    | 说明                                  | 示例                             |
| ----------------------- | ------------------------------------- | -------------------------------- |
| `-f`,`--locustfile` | 指定 Locust 测试文件                  | `-f locustfile.py`             |
| `--host`              | 被测系统的主机地址                    | `--host http://localhost:8000` |
| `--users`             | 启动时模拟的用户数（并发用户）        | `--users 100`                  |
| `--spawn-rate`        | 用户启动速率（每秒新增用户数）        | `--spawn-rate 10`              |
| `--headless`          | 无 Web UI 模式（适合自动化）          | `--headless`                   |
| `--run-time`          | 执行时间，支持 `s`,`m`,`h`      | `--run-time 1m30s`             |
| `--csv`               | 输出性能报告（CSV格式，指定文件前缀） | `--csv result`                 |
| `--html`              | 输出 HTML 报告                        | `--html report.html`           |
| `--logfile`           | 指定日志文件路径                      | `--logfile locust.log`         |
| `--loglevel`          | 日志级别（DEBUG、INFO、WARNING）      | `--loglevel INFO`              |
| `--tags`              | 只运行带指定 tag 的任务               | `--tags tag1,tag2`             |
| `--exclude-tags`      | 排除带指定 tag 的任务                 | `--exclude-tags slow`          |
| `--web-host`          | Web UI 服务监听地址                   | `--web-host 0.0.0.0`           |
| `--web-port`          | Web UI 服务监听端口                   | `--web-port 8089`              |
