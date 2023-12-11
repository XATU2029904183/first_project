def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

# 输入要计算的斐波那契数列长度
length = int(input("请输入斐波那契数列的长度："))

# 调用函数计算斐波那契数列
fib_sequence = fibonacci(length)

# 输出结果
print("斐波那契数列：", fib_sequence)