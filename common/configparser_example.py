from configparser import ConfigParser, NoOptionError

# 读取配置文件
cfg = ConfigParser()
cfg.read('config.ini')

# 打印配置文件中的模块
sections = cfg.sections()
print(sections)

# 获取模块中的参数，默认为字符串类型
server_hostname = cfg.get('databricks', 'server_hostname')
print(server_hostname)
print(type(server_hostname))

# 获取int型参数
try:
    workers = cfg.getint('server', 'workers')
except NoOptionError as err:
    print(type(err).__name__)

print(workers)
print(type(workers))
