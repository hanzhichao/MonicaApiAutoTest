from apis.base_api import BaseApi
from apis.contacts_api import ContactsApi


class Api(BaseApi):
    def __init__(self, token, base_url=None):
        super().__init__(token, base_url)
        self.contacts = ContactsApi(token, base_url)
