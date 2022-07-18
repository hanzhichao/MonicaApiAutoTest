import logging
import json
import csv
import yaml

class FileUtils:
    def read(self, file_path, encoding='utf-8'):
        """读取纯文本文件全部内容"""
        logging.debug('读取文本文件: %s' % file_path)
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    def load_txt(self, file_path, encoding='utf-8'):
        """读取txt文件并得到每一数据组成的列表"""
        logging.debug('加载TXT文件: %s' % file_path)
        with open(file_path, 'r', encoding=encoding) as f:
            return [row.strip() for row in f.readlines()]

    def load_json(self, file_path, encoding='utf-8'):
        """加载json文件并转为字典或列表，如果json文件不合法，会报JSONDecodeError"""
        logging.debug('加载JSON文件: %s' % file_path)
        with open(file_path, 'r', encoding=encoding) as f:
            return json.load(f)

    def load_yaml(self, file_path, encoding='utf-8'):
        """加载yml文件并转为字典或列表，需要安装PyYAML"""
        logging.debug('加载YAML文件: %s' % file_path)
        with open(file_path, 'r', encoding=encoding) as f:
            return yaml.safe_load(f)


    def load_csv(self, file_path, encoding='utf-8', delimiter=",", with_header=True):
        """加载csv文件，并返回列表，默认文件带标题行with_header=True"""
        logging.debug('加载CSV/TSV文件: %s' % file_path)
        data = []
        with open(file_path, 'r', encoding=encoding) as f:
            if with_header is True:
                reader = csv.DictReader(f, delimiter=delimiter)
            else:
                reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                data.append(row)
        return data

    def load(self, file_path, **kwargs):
        """加载任意支持的数据文件"""
        file_path = str(file_path)  # 将Path类型转为路径字符串
        if file_path.endswith('.txt'):
            return self.load_txt(file_path, **kwargs)
        elif file_path.endswith('.csv'):
            return self.load_csv(file_path, **kwargs)
        elif file_path.endswith('.tsv'):
            return self.load_csv(file_path, delimiter='\t', **kwargs)
        elif file_path.endswith('.json'):
            return self.load_json(file_path, **kwargs)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return self.load_yaml(file_path, **kwargs)
        else:
            raise NotImplementedError('不支持该文件类型')
