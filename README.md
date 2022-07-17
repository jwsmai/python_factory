# Python Factory

## 使用[configparser](common/configparser_example.py)从配置文件获取参数

相关链接：

- https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p10_read_configuration_files.html

## 使用[getopt](common/getopt_example.py)从命令行获取参数

### Highline

从命令行读取的参数默认是str类型，这里用`int()`函数将它转化为int类型

### 相关链接

- https://www.geeksforgeeks.org/getopt-module-in-python/
- https://docs.python.org/zh-cn/3/library/getopt.html

## 使用[loguru](common/loguru_example.py)记录日志

### Highline

#### 使用`@logger.catch`代替`try catch`跟踪变量的值

代码：

```python
@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(1, -1, 0)
```

日志：

```md
2022-07-17 16:58:34.814 | ERROR | __main__:<module>:21 - An error has been caught in function '<module>', process '
MainProcess' (14074), thread 'MainThread' (4335273344):
Traceback (most recent call last):

> File "/Users/suwenjin/Documents/GitWarehouse/python_factory/common/loguru_example.py", line 21, in <module>
my_function(1, -1, 0)
└ <function my_function at 0x126cac790>

File "/Users/suwenjin/Documents/GitWarehouse/python_factory/common/loguru_example.py", line 18, in my_function
return 1 / (x + y + z)
│ │ └ 0
│ └ -1
└ 1

ZeroDivisionError: division by zero

Process finished with exit code 0
```

#### 日志分割

loguru日志太多时，可以根据不同的策略保存日志

- 每500MB创建一个文件

```python
logger.add('runtime_{time}.log', rotation="500 MB")
```

- 每周创建一个日志

```python
logger.add('runtime_{time}.log', rotation='1 week')

```

- 每天零点创建日志

```python
logger.add('runtime_{time}.log', rotation='00:00')
```

### 相关链接

- https://loguru.readthedocs.io/en/stable/api/logger.html
- https://cuiqingcai.com/7776.html

## 创建和判断inf、nan

### 代码

```python
import math

# 创建无穷大、负无穷大的浮点值
a = float('inf')
b = float('-inf')

# 创建非数字的nan
c = float('nan')

print(a, b, c)

# 判断inf、 -inf、 nan
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))
```

### 相关链接

- https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p07_infinity_and_nan.html

## 使用[Databricks SQL Connector](databricks/databricks_utils.py)查询databricks数据

### 相关链接

- https://docs.databricks.com/dev-tools/python-sql-connector.html