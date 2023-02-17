yaer = int(input("Введите год "))

if(yaer %4 == 0 and yaer % 100 != 0) or yaer % 400 == 0:
    februrary = 29
else: februrary = 28
GGWP = 0
array = [31, februrary, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(12):
    for c in range(array[i]+1):
        GGWP += c//10 + c%10
print(GGWP)