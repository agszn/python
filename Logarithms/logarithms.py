import math

# Common logarithm (base 10)
print(math.log10(100))  # Output: 2.0

# Natural logarithm (base e)
print(math.log(math.e ** 2))  # Output: 2.0

# Binary logarithm (base 2)
print(math.log2(8))  # Output: 3.0

# Change of base formula
base_10_log = math.log10(8)
base_2_log = base_10_log / math.log10(2)
print(base_2_log)  # Output: 3.0
