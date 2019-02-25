import yaml
import os


class YamlReader:

    def __init__(self,yamlfile):
        self._data = list()
        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile
        else:
            raise FileNotFoundError('文件不存在！')
            self._data = None

    @property
    def data(self):

        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
         if not self._data:
            with open(self.yamlfile, 'r') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
         return self._data








