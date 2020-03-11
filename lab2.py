# 问题1 求平方根

def average(x, y):
    return (x + y)/2

square = lambda x: x * x

def sqrt_update(guess, x):
    return average(guess, x/guess)

"""程序中测试相似性的一个常见方式是将数值差的绝对值与一个微小的公差值相比"""
def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

"""重复调用update函数来改进这个推测值，并且调用test来检查是否当前的guess“足够接近”所认为的正确值"""
def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess

def square_root(x):
    def update(guess):
        return average(guess, x/guess)
    def test(guess):
        return approx_eq(square(guess), x)
    return iter_improve(update, test)

# 问题2 lambda表达式
s = lambda x: x + 1
print(s(12));

# 问题3 高阶函数&装饰器

def wrapper(fn):
    def f(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return f;

@wrapper
def a(x):
    return x

a(12);

# 问题4 Lambdas and Currying
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    def fn(x):
        return lambda y: func(x, y);
    return fn;

from operator import add

curried_add = lambda_curry2(add)

add_three = curried_add(56)

print(add_three(5));

# 问题5 Composite Identity Function
def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    def fn(x):
        return f(g(x));
    return fn;
add_one = lambda x: x + 1 
square = lambda x: x**2
a1 = compose1(square, add_one)
mul_three = lambda x: x * 3 
a2 = compose1(mul_three, a1)
print(a2(5));

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    return lambda x: f(g(x))== g(f(x))

b1 = composite_identity(square, add_one)
print(b1(4));

# 问题6
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def countDef(n):
        i,count = 1,0
        while i <= n:
            if condition(n, i):
                count += 1;s
            i += 1;
        return count;
    return countDef;
    
count_factors = count_cond(lambda n, i: n % i == 0)
print(count_factors(12))