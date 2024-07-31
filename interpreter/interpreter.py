expr = input("Expression: ")

x , y , z = expr.split()
x = int(x)
z = int(z)

if "+" in expr:
    ans = x + z
elif "-" in expr:
    ans = x - z
elif "/" in expr:
    ans = x / z
elif "*" or "x" in expr:
    ans = x * z

print(float(ans))