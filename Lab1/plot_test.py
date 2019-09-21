import matplotlib.pyplot as plt

x =[2, 10, 20, 50 , 100 ]
y = [24, 30, 35, 40, 50]

f = plt.figure(1)
plt.plot(x, y, label="k vs error Line")
plt.xlabel('K')
plt.ylabel('Absolute error')
plt.title('Two lines on same graph!')


x =[500, 400, 300, 200 , 100 ]
y = [24, 30, 35, 40, 50]
p = plt.figure(2)
plt.plot(x, y, label="k vs error Line")
plt.xlabel('K')
plt.ylabel('Absolute error')
plt.title('Two lines on same graph!')

plt.show()

input()