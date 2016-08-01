# Hello World
print("Hello World!");

print("variable...")
# variable
name = input("please enter your name: ");
print("Hello,",name,"!");

print("if statements...")
# if statements
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print("Negative changed to zero!")
elif x == 0:
	print("Zero")
elif x == 1:
	print("Single")
else:
	print("More")

print("for statements...")
# for statements
a = ["cat", "dog", "pig"]
for x in a:
	print(x, len(x))

print("break and 循环中的else...")
# break and 循环中的else
# 循环可以有一个 else 子句；它在循环迭代完整个列表（对于 for ）或执行条件为 false （对于 while ）时执行，
# 但循环被 break 中止的情况下不会执行。
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, "equal", x, "*", n//x)
			break
	# 这个else语句对应的第二个for循环（不是最近的if语句），它会在第二个for循环执行完时执行，
	# 但循环被break中止的情况下不会执行。		
	else:
			print(n, "is a prime number")
			
print("continue...")
# continue
for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)
	
print("pass statements...")
print("pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合，",
"另一方面， pass 可以在创建新代码时用来做函数或控制体的占位符。")
# pass statements
# while True:
#	pass

print("function define...")
def fib2(n):
	"返回斐波那契数列数字列表"
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
	
print("调用 fib2()方法……")
# f100 = fib2(100)
# f100