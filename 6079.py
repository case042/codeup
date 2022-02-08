n = int(input())
result = 0
cnt = 1
while True:
    result += cnt
    if n <= result:
        break
    cnt+=1

print(cnt)