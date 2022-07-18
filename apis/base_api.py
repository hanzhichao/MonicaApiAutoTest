"""接口封装的基础类-完成GET、POST请求封装以及登录授权等"""
import logging

import requests


class BaseApi:
    def __init__(self, token=None, base_url=None):
        self.token = token
        self.base_url = base_url
        self.session = requests.Session()
        if token is not None:
            self.auth()
        
    def auth(self):
        self.session.headers['Authorization'] = 'Bearer %s' % self.token

    def request(self, method, url, *args, **kwargs):
        logging.debug(f'{method} {url}')
        if isinstance(url, str) and not url.startswith('http'):
            url = self.base_url + url
        return self.session.request(method, url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        return self.request('GET', url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self.request('POST', url, *args, **kwargs)
    
    def put(self, url, *args, **kwargs):
        return self.request('POST', url, *args, **kwargs)
    
    def delete(self, url, *args, **kwargs):
        return self.request('DELETE', url, *args, **kwargs)
