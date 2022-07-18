import logging
import pymysql


class MysqlUtils:
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        logging.debug('连接数据库 %s' % host)
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    port=port,
                                    db=db,
                                    charset=charset,
                                    autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def query(self, sql):
        """执行查询sql并返回所有查询结果List(Dict)"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        logging.info('查询SQL：%s 结果 %s' % (sql, result))
        return result

    def execute(self, sql):
        """执行修改sql并返回影响行数"""
        try:
            result = self.cur.execute(sql)
        except Exception as ex:
            logging.exception(ex)
            self.conn.rollback()
        else:
            logging.debug('执行修改SQL：%s 影响行数 %s' % (sql, result))
            return result

    def close(self):
        logging.debug('断开数据库连接')
        self.cur.close()
        self.conn.close()
