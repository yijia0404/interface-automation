import pytest
from common import yamlUtility
from core.requestsUtility import RequestsUtility
import pytest_check
import allure
import logging


class TestMain:
    data = yamlUtility.read_all_yaml("/Users/yijia/PycharmProjects/pythonProject2/testcase")

    @pytest.mark.parametrize("test_data", data)
    def test_run(self, test_data):
        print(f"开始执行 {test_data[0]['name']} 测试用例")
        name = test_data[0]["name"]
        method = test_data[0]["method"]
        url = test_data[0]["url"]
        data = test_data[0]["data"]
        feature = test_data[0]["feature"]
        allure.dynamic.title(name)
        allure.dynamic.feature(feature)
        allure.dynamic.story(feature + " story")
        allure.dynamic.suite(feature)
        allure.dynamic.sub_suite(feature + " sub_suite")
        res = RequestsUtility().request(method, url, data, timeout=1)
        assert "maxlength" in res.text
        pytest_check.is_in("maxlength", res.text, "maxlength 不能找到")
        pytest_check.is_in("asdf", res.text, "asdf 不能找到")
        print(f"结束执行 {test_data[0]['name']} 测试用例")


if __name__ == '__main__':
    pytest.main(["-vs", "--alluredir=/Users/yijia/PycharmProjects/pythonProject2/alluretemp",
                 "/Users/yijia/PycharmProjects/pythonProject2/testcase"])
    # pytest.main(["-vs", "/Users/yijia/PycharmProjects/pythonProject2/testcore"])
