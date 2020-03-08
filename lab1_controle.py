"""Lab 1: Expressions and Control Structures"""

# http://inst.eecs.berkeley.edu/~cs61a/fa17/lab/lab01/#what-would-python-display-part-1

# Coding Practice

# 问题1 重复
"""def repeated(f, n, x):
    Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    *** YOUR CODE HERE ***"""
def square(x):
    return x * x;

def opposite(b):
    return not b;

def repeated(f, n, x):
    total = x;
    i = 0;
    while i < n:
        total = f(total);
        i += 1;
    return total;

repeated(square, 2, 3)

repeated(square, 1, 4)

repeated(square, 6, 2)

repeated(opposite, 4, True)

# 问题2 总位数
"""def sum_digits(n):
    Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    *** YOUR CODE HERE ***"""
def sum_digits(n):
    result = 0;
    for i in str(n):
        result += int(i);
    print(result);
    
sum_digits(1234567890)

# 问题3 双8
"""def double_eights(n):
    Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    *** YOUR CODE HERE ***"""
def double_eights(n):
    result = 0;
    for i in str(n):
        if(int(i) == 8):
            result += 1;
    if(result > 2):
        return False;
    else:
        return True;
            
double_eights(12131231)


# 问题4 修复错误
"""def both_positive(x, y):
    Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
def both_positive(x, y):
    return x > 0 and y > 0
    
both_positive(-1, 1)

# 问题6 下降阶乘
"""def falling(n, k):
    Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
def falling(n, k):
    i = 1;
    total = n;
    a = n
    if(k == 0):
        return 1;
    while i < k:
        a -= 1;
        total *= a;
        i += 1;
    return total;

falling(4, 3);

# 问题7 