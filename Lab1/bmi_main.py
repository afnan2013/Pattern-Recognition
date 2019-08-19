n = int(input("Please enter the number of TRAIN DATA : "))

print("Please enter the height(inches) and weight(kilogram) and class(O=Overweight, N=Normal ,U= Underweight) of TRAIN DATA in a row")

h = []
w = []
c = []

for i in range(n):
    h1, w1, c1 = input().split()
    h.append(int(h1))
    w.append(int(w1))
    c.append(c1)

print("\n\nPlease enter the height(inches) and weight(kilogram) of TEST DATA")

text = 3
for j in range(text):
    h1, w1 = input().split()
    H = int(h1)
    W = int(w1)

    result = 100001
    index = -1
    
    for i in range(n):
        u_distance = (h[i]-H)*(h[i]-H) + (w[i]-W)*(w[i]-W)
        if u_distance < result:
            result = u_distance
            index = i

    print("\nThe test data you inputed is of Class : ", c[index])