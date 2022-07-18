from apis.base_api import BaseApi


class ContactsApi(BaseApi):
    def get_contact_list(self, limit=None, page=None, query=None, sort=None):
        """
        查询联系人列表
        :param limit: 限制返回的查询条数
        :param page: 查询结果的页码
        :param query: 查询关键词，为None时返回所有
        :param sort: 排序方式，支持created_at, -created_at, updated_at, -updated_at
        :return:
        """
        url = '/api/contacts'
        res = self.get(url, params=dict(limit=limit, page=page, query=query, sort=sort))
        return res.json()

    def get_contact_detail(self, contact_id):
        """
        获取联系人详情
        :param contact_id: 联系人Id
        :return:
        """
        url = '/api/contacts/%d' % contact_id
        res = self.get(url)
        return res.json()

    def create_contact(self, first_name, last_name=None, nickname=None, gender_id=1, birthdate_day=None,
                       birthdate_month=None, birthdate_year=None, is_birthdate_known=False,
                       birthdate_is_age_based=True, birthdate_age=None, is_partial=False,
                       is_deceased=False, deceased_date_day=None, deceased_date_month=None, deceased_date_year=None,
                       deceased_date_is_age_based=True, is_deceased_date_known=False):
        """
        创建联系人
        :param first_name: 联系人名
        :param last_name: 联系人姓
        :param nickname: 联系人别名
        :param gender_id: 性别Id，1-男性 2-女性 3-跨性别
        :param birthdate_day: 生日-天
        :param birthdate_month: 生日-月
        :param birthdate_year: 生日-年
        :param is_birthdate_known: 是否知道生日
        :param birthdate_is_age_based: 是否使用周岁
        :param birthdate_age: 周岁年龄
        :param is_partial: 是否偏爱的
        :param is_deceased: 是否去世
        :param deceased_date_day: 去世时间-天
        :param deceased_date_month: 去世时间-月
        :param deceased_date_year: 去世时间-年
        :param deceased_date_is_age_based: 基于去世时间计算年龄
        :param is_deceased_date_known: 是否知道去世时间
        :return:
        """
        url = '/contacts/'
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "gender_id": gender_id,
            "birthdate_day": birthdate_day,
            "birthdate_month": birthdate_month,
            "birthdate_year": birthdate_year,
            "is_birthdate_known": is_birthdate_known,
            "birthdate_is_age_based": birthdate_is_age_based,
            "birthdate_age": birthdate_age,
            "is_partial": is_partial,
            "is_deceased": is_deceased,
            "deceased_date_day": deceased_date_day,
            "deceased_date_month": deceased_date_month,
            "deceased_date_year": deceased_date_year,
            "deceased_date_is_age_based": deceased_date_is_age_based,
            "is_deceased_date_known": is_deceased_date_known,
        }
        res = self.post(url, json=payload)
        return res.json()

    def update_contact(self, contact_id, first_name, last_name=None, nickname=None, gender_id=1, birthdate_day=None,
                       birthdate_month=None, birthdate_year=None, is_birthdate_known=False,
                       birthdate_is_age_based=True, birthdate_age=None, is_partial=False,
                       is_deceased=False, deceased_date_day=None, deceased_date_month=None, deceased_date_year=None,
                       deceased_date_is_age_based=True, is_deceased_date_known=False):
        """
        创建联系人
        :param contact_id: 联系人Id
        :param first_name: 联系人名
        :param last_name: 联系人姓
        :param nickname: 联系人别名
        :param gender_id: 性别Id，1-男性 2-女性 3-跨性别
        :param birthdate_day: 生日-天
        :param birthdate_month: 生日-月
        :param birthdate_year: 生日-年
        :param is_birthdate_known: 是否知道生日
        :param birthdate_is_age_based: 是否使用周岁
        :param birthdate_age: 周岁年龄
        :param is_partial: 是否偏爱的
        :param is_deceased: 是否去世
        :param deceased_date_day: 去世时间-天
        :param deceased_date_month: 去世时间-月
        :param deceased_date_year: 去世时间-年
        :param deceased_date_is_age_based: 基于去世时间计算年龄
        :param is_deceased_date_known: 是否知道去世时间
        :return:
        """
        url = '/api/contacts/%d' % contact_id
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "gender_id": gender_id,
            "birthdate_day": birthdate_day,
            "birthdate_month": birthdate_month,
            "birthdate_year": birthdate_year,
            "is_birthdate_known": is_birthdate_known,
            "birthdate_is_age_based": birthdate_is_age_based,
            "birthdate_age": birthdate_age,
            "is_partial": is_partial,
            "is_deceased": is_deceased,
            "deceased_date_day": deceased_date_day,
            "deceased_date_month": deceased_date_month,
            "deceased_date_year": deceased_date_year,
            "deceased_date_is_age_based": deceased_date_is_age_based,
            "is_deceased_date_known": is_deceased_date_known,
        }
        res = self.put(url, json=payload)
        return res.json()

    def delete_contact(self, contact_id):
        """
        删除联系人
        :param contact_id: 联系人Id
        :return:
        """
        url = '/api/contacts/%d' % contact_id
        res = self.delete(url)
        return res.json()

