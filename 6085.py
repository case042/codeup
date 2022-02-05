w,h,b = list(map(int, input().split()))

t = w*h*b/8/1024/1024
result = round(t,2)

if len(str(result)) == 3:
    x = str(result)
    x += "0"
    result = x
print(result,"MB")