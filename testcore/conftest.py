import pytest
import requests
import os


@pytest.fixture(scope="session", autouse=True)
def get_session():
    os.system("rm -rf /Users/yijia/PycharmProjects/pythonProject2/alluretemp/*")
    os.system("rm -rf /Users/yijia/PycharmProjects/pythonProject2/report/*")
    print("获取session")
    requests.request("get", "https://www.baidu.com")
