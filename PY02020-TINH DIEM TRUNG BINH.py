#by sekido
mx_value = -1
mn_value = 11
n = int(input())
a = [float(i) for i in input().split()]
mx_value = max(a)
mn_value = min(a)
res = 0.0
count = 0
for v in a :
    if (v != mn_value and v != mx_value) :
        res += v
        count += 1
res = res / count
print(f"{res:.2f}")