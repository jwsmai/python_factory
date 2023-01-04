import re

with open('ddl.sql', 'rt') as f:
    data = f.read()
    # 获取表名
    table_name = re.findall('ads.*f', data)
    # 替换not null
    data = re.sub('(NOT|not)\s+(NULL|null)', '', data)
    # 替换primary key
    data = re.sub('(primary\s+key)|auto_increment|(default\s+0)', '', data)
    # 替换null
    data = re.sub('(NULL|null)', '', data)
    # 替换字符串类型
    data = re.sub('varchar\(\d+\)', 'STRING', data)
    # 替换datetime类型
    data = re.sub('datetime\(\d+\)', 'TIMESTAMP', data)
    # 替换text类型
    data = re.sub('text', 'STRING', data)
    # 替换text类型
    data = re.sub('tinyint', 'boolean', data)
    # 替换浮点数类型
    data = re.sub('decimal\(.*\d\)', 'DOUBLE', data)
    # 替换UNIQUE KEY定义
    data = re.sub('UNIQUE.*\)', '', data)
    # 替换DISTRIBUTED定义
    data = re.sub('DISTRIBUTED.*\;', '', data)
    print(data)
