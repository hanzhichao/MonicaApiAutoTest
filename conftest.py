import os
import platform
from datetime import datetime


import pytest
import requests
import pytest_check

from apis.api import Api
from services.monica_db import MonicaDb
from utils.email_utils import EmailUtils
from utils.mysql_utils import MysqlUtils
from apis.contacts_api import ContactsApi


NOW = datetime.now()


def pytest_addoption(parser):
    parser.addoption('--send_email', action="store_true", help='auto send email or not')


def pytest_configure(config):
    """Pytest初始化配置钩子函数"""
    root_dir = config.rootpath  # 获取项目根目录

    # 获取pytest.ini文件中的log_file配置项
    log_file = config.getini('log_file')
    if log_file:  # 如果存在该配置项2
        # 修改命令行选项中的log-file参数为日志绝对路径
        config.option.log_file = root_dir / NOW.strftime(log_file)

    # 处理allure报告路径
    alluredir = config.getoption("--alluredir")
    if alluredir is not None:
        config.option.allure_report_dir = root_dir / alluredir


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if config.getoption("--alluredir") is not None:
        if 'Windows' in platform.platform():
            allure = config.rootpath / 'tools/allure-2.18.1/bin/allure.bat'
        else:
            allure = config.rootpath / 'tools/allure-2.18.1/bin/allure'

        allure_data = config.option.allure_report_dir
        allure_html = config.rootpath / 'reports/allure-html'
        os.system('%s generate %s -o %s' % (allure, allure_data, allure_html))
        print('allure html报告生成成功')

    # 执行完用例根据参数自动发送邮件
    if config.getini('send_email'):
        attachments = [config.option.log_file]  # 默认邮件附件中添加执行日志文件
        if config.getini('gen_report'):
            # 邮件附件中添加生成到HTML报告目录，目录自动压缩
            attachments.append(config.allure_report_dir)

        ini = config.ini  # pytest-ini插件在config中添加了pytest.ini的ConfigParser对象
        smtp_server = ini.get('smtp', 'smtp_server')
        smtp_user = ini.get('smtp', 'smtp_user')
        smtp_password = ini.get('smtp', 'smtp_password')
        smtp_port = ini.get('smtp', 'smtp_port')
        enable_ssl = ini.get('smtp', 'enable_ssl')
        subject = ini.get('email', 'email_subject')
        body = ini.get('email', 'email_body')
        receivers = ini.get('email', 'email_receivers').split(',')
        receivers = [item.strip() for item in receivers]

        EmailUtils(smtp_server, smtp_user, smtp_password, smtp_port, enable_ssl) \
            .send_email(subject, receivers, body, attachments=attachments)


@pytest.fixture
def base_url(env_vars):
    """返回pytest.ini指定环境中的base_url变量，需要安装pytest-ini"""
    return env_vars.get('base_url')


@pytest.fixture
def token(env_vars):
    """返回pytest.ini指定环境中的token变量，需要安装pytest-ini"""
    return env_vars.get('token')


@pytest.fixture
def db_conf(env_vars):  # need pip install pytest-ini
    host = env_vars.get('db_host')
    port = env_vars.get('db_port')
    user = env_vars.get('db_user')
    password = str(env_vars.get('db_password'))
    db = env_vars.get('db_name')
    return dict(host=host, port=port, user=user, password=password, db=db)


@pytest.fixture
def db(db_conf):
    return MysqlUtils(**db_conf)


@pytest.fixture
def monica_db(db_conf):
    return MonicaDb(**db_conf)


@pytest.fixture
def session(token):
    session = requests.Session()
    session.headers['Authorization'] = 'Bearer %s' % token
    return session


@pytest.fixture
def api(token, base_url):
    return Api(token, base_url)


@pytest.fixture()
def check():
    return pytest_check


@pytest.fixture
def contacts_api(token, base_url):
    return ContactsApi(token, base_url)
