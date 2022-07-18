from utils.mysql_utils import MysqlUtils


class MonicaDb(MysqlUtils):

    def count_contacts(self):
        return self.query('select count(id) as total from contacts')[0]['total']
