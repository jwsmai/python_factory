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
