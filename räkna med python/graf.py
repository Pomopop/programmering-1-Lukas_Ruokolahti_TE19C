#import matplotlib.pyplot as plt


#s = [10,20,30,40,50,60,70,80,90,100]
#t = [1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.94, 8.79, 9.69]

#plt.plot(s, t, '*-')
#plt.xlabel("sträcka")
#plt.ylabel("tid")
#plt.title("s-t-diagram")

#plt.show()

import matplotlib.pyplot as plt

s = [10,20,30,40,50,60,70,80,90,100]
t = [1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.94, 8.79, 9.69]
v = [0]

for i in range(1, len(t)):
    v_i = (s[i]-s[i-1])/(t[i]-t[i-1])
    v.append(v_i)
   # print(i)

print(len(v))
print(len(t))

plt.plot(t, v, '*-')
plt.title("Usain bolt 100m V-T graf")
plt.xlabel("tid")
plt.ylabel("hastighet")
plt.grid()
plt.show()