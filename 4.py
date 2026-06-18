# int>str
print(str(22))

# int>float
print(float(22))

# int>bool
print(bool(22))  # true
print(bool(-22))  # true
print(bool(0))  # False

# float
# float>int
print(int(15.4))  # 15
print(int(15.5))  # 15
print(int(15.999999999))  # 15
print(int(15.99999999999999999))  # 16

# float> str
print(str(5.55))  # 5.55

# float>bool
print(bool(1.4))  # True
print(bool(0.1))  # True
print(bool(15.999999999))  # True
print(bool(0.00000000000000000000000001))  # True
print(bool(0.0))  # false

# bool
# bool>str
print(str(True))  # True
print(str(False))  # False
print(bool(str(False)))  # True

# bool>int
print(int(True))  # 1
print(int(False))  # 0

# bool>float
print(float(True))  # 1.0
print(float(False))  # 0.0

##################

# Оператор + - * / // % **      математичні оператори

#                5          +           5       бінарний оператор
#           операнд      оператор    операнд

#                           -           5       унарний оператор
#                        оператор    операнд

# () : Parentheses (highest precedence) -> Associativity: Left to right
# x[index], x[index:index] : Subscription, slicing -> Associativity: Left to right
# await x : Await expression
# ** : Exponentiation -> Associativity: Right to left
# +x, -x, ~x : Unary plus, unary minus, bitwise NOT -> Associativity: Right to left
# *, @, /, //, % : Multiplication, matrix multiplication, division, floor division, remainder -> Associativity: Left to right
# +, - : Addition and subtraction -> Associativity: Left to right
# <<, >> : Bitwise shifts -> Associativity: Left to right
# & : Bitwise AND -> Associativity: Left to right
# ^ : Bitwise XOR -> Associativity: Left to right
# | : Bitwise OR -> Associativity: Left to right
# in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, membership, identity tests -> Associativity: Left to right
# not x : Boolean NOT -> Associativity: Right to left
# and : Boolean AND -> Associativity: Left to right
# or : Boolean OR -> Associativity: Left to right
# if-else : Conditional expression -> Associativity: Right to left
# lambda : Lambda expression
# := : Assignment expression (Walrus operator) -> Associativity: Right to left

n = 2 + 2 - 4 + 433 * 3 - 3 - 4
print(n)
print(str(n))

a = 4
b = 2
print('{}+{}={}'.format(a, b, a + b))
print(f"{a} + {b} = {a + b}")  # Python > 3.6
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# Теорема Піфагора
print(f"{a * a} + {b * b} = {a * a + b * b}")

a = 2
b = 3

# square.png
print(f"{a * a * a} + {b * b * b} = {(a + b) * (a * a - a * b + b * b)}")

