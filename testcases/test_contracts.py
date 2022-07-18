"""测试Monica联系人接口"""
from pprint import pprint

import allure
import pytest
import pytest_check


@allure.feature("联系人管理")
class TestMonicaContactsApi:
    @pytest.mark.level(1)
    @pytest.mark.owner('hzc')
    @allure.story("获取联系人列表")
    def test_get_contact_list(self, base_url, session, db):
        url = f'{base_url}/api/contacts'
        res_dict = session.get(url).json()
        pprint(res_dict)

        total = res_dict['meta']['total']
        db_total = db.query('select count(id) as total from contacts')[0]['total']
        pytest_check.equal(total, db_total, msg=f'接口联系人数量{total}应与数据库联系人数量{db_total}相等')

    def test_get_contact_list_02(self, contacts_api, check):
        res_dict = contacts_api.get_contracts_list()
        print(res_dict)

    def test_get_contact_list_03(self, api, check):
        res_dict = api.contacts.get_contracts_list()
        print(res_dict)

    def test_get_contact_list_04(self, api, monica_db, check):
        res_dict = api.contacts.get_contracts_list()
        total = res_dict['meta']['total']
        db_total = monica_db.count_contacts()
        check.equal(total, db_total, msg=f'接口联系人数量{total}应与数据库联系人数量{db_total}相等')
