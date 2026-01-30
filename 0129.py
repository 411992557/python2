import math
print(math.floor(3.5))

print(math.sin(1))



print(math.comb(5,2))

print(math.factorial(5))

# 1. math.comb(n, k) - 组合数计算
# 示例：从5个元素中选2个的组合数，k>n时返回0

print(f"math.comb(5, 2) = {math.comb(5, 2)}")  # 输出 10
print(f"math.comb(5, 6) = {math.comb(5, 6)}")  # 输出 0（k>n时为0）

# 2. math.factorial(n) - 阶乘计算（仅非负整数）
# 示例：5的阶乘，注意浮点数形式的整数（如5.0）
print(f"math.factorial(5) = {math.factorial(5)}")  # 输出 120

# 3. math.gcd(*integers) - 最大公约数
# 示例：多个整数的最大公约数，全0返回0，无参数返回0
print(f"math.gcd(12, 18, 24) = {math.gcd(12, 18, 24)}")  # 输出 6
print(f"math.gcd(0, 0) = {math.gcd(0, 0)}")              # 输出 0

# 4. math.isqrt(n) - 整数平方根（向下取整）
# 示例：10的整数平方根（3²=9≤10，4²=16>10），上限平方根计算
print(f"math.isqrt(10) = {math.isqrt(10)}")              # 输出 3
print(f"1 + math.isqrt(10 - 1) = {1 + math.isqrt(10 - 1)}")  # 输出 4（上限平方根）

# 5. math.lcm(*integers) - 最小公倍数
# 示例：多个整数的最小公倍数，含0返回0，无参数返回1
print(f"math.lcm(4, 6, 8) = {math.lcm(4, 6, 8)}")  # 输出 24
print(f"math.lcm(4, 0) = {math.lcm(4, 0)}")          # 输出 0（含0时为0）

# 6. math.perm(n, k) - 排列数计算
# 示例：从5个元素中选3个的排列数，k>n时返回0，k默认等于n时返回n!
print(f"math.perm(5, 3) = {math.perm(5, 3)}")  # 输出 60
print(f"math.perm(5) = {math.perm(5)}")        # 输出 120（等价于5!）
print(f"math.perm(5, 6) = {math.perm(5, 6)}")  # 输出 0（k>n时为0）







# 1. math.cbrt(x) - 立方根计算（支持正负值）
# 示例：8的立方根、-8的立方根
print(f"math.cbrt(8) = {math.cbrt(8)}")      # 输出 2.0
print(f"math.cbrt(-8) = {math.cbrt(-8)}")    # 输出 -2.0

# 2. math.exp(x) - 自然指数e^x（精度高于math.e**x）
# 示例：e^1、e^2的计算
print(f"math.exp(1) = {math.exp(1)}")        # 输出 ≈2.718281828459045
print(f"math.exp(2) = {math.exp(2)}")        # 输出 ≈7.38905609893065

# 3. math.exp2(x) - 2的x次幂
# 示例：2^3、2^5的计算
print(f"math.exp2(3) = {math.exp2(3)}")      # 输出 8.0
print(f"math.exp2(5) = {math.exp2(5)}")      # 输出 32.0

# 4. math.expm1(x) - e^x - 1（小数值计算精度更高）
# 示例：对比exp(x)-1和expm1(x)的精度（x=1e-5）
x_small = 1e-5
print(f"exp({x_small}) - 1 = {math.exp(x_small) - 1}")  # 精度损失：≈1.0000050000069649e-05
print(f"math.expm1({x_small}) = {math.expm1(x_small)}") # 全精度：≈1.0000050000166668e-05

# 5. math.log(x[, base]) - 对数计算（单参数为自然对数，双参数指定底数）
# 示例：自然对数ln(10)、以2为底log2(8)、以10为底log10(100)
print(f"math.log(math.e) = {math.log(math.e)}")          # 输出 1.0（自然对数）
print(f"math.log(8, 2) = {math.log(8, 2)}")              # 输出 3.0（指定底数）

# 6. math.log1p(x) - ln(1+x)（x接近0时精度更高）
# 示例：x=1e-5时ln(1+x)的高精度计算
print(f"math.log1p({x_small}) = {math.log1p(x_small)}")  # 输出 ≈1.0000049999833334e-05

# 7. math.log2(x) - 以2为底的对数（精度高于math.log(x,2)）
# 示例：log2(16)、log2(10)的计算
print(f"math.log2(16) = {math.log2(16)}")    # 输出 4.0
print(f"math.log2(10) = {math.log2(10)}")    # 输出 ≈3.3219280948873626

# 8. math.log10(x) - 以10为底的对数（精度高于math.log(x,10)）
# 示例：log10(100)、log10(2)的计算
print(f"math.log10(100) = {math.log10(100)}")  # 输出 2.0
print(f"math.log10(2) = {math.log10(2)}")      # 输出 ≈0.3010299956639812

# 9. math.pow(x, y) - x的y次幂（遵循IEEE 754标准，支持非整数幂）
# 示例：2^3、0^0（返回1.0）、负数的非整数幂（报错）
print(f"math.pow(2, 3) = {math.pow(2, 3)}")    # 输出 8.0
print(f"math.pow(0, 0) = {math.pow(0, 0)}")    # 输出 1.0（IEEE 754标准）

# 10. math.sqrt(x) - 平方根计算（仅非负数）
# 示例：16的平方根、2的平方根
print(f"math.sqrt(16) = {math.sqrt(16)}")      # 输出 4.0
print(f"math.sqrt(2) = {math.sqrt(2)}")        # 输出 ≈1.4142135623730951