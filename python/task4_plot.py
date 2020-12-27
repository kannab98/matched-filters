import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 


df = pd.read_excel('task4.xlsx', engine='openpyxl')
print(df)


# Число реализаций
N = 20
# Шаг по длительности
step = 5
t =  np.arange(10, 100, 1)
tau = np.array([np.arange(10, 100, 1) for i in range(N)])
tau = np.sort(tau.flatten())



out = df["out"].values 
outm = df["out_mean"].values 
print(out.shape, tau.shape)

# index = np.where(~np.isnan(out))
# outm = outm[index]
# out = out[index]
# tau = tau[index]

index = np.where(out > 100)
outm = outm[index]
out = out[index]
tau = tau[index]

index = np.where((out > 100) & (out < 2000) )
outm = outm[index]
out = out[index]
tau = tau[index]

index = np.where((outm > 100) & (outm < 2000) )
outm = outm[index]
out = out[index]
tau = tau[index]



Index = np.array([])
U = []
Um = []
T = []

for i in range(t.size):
    index = np.where(tau == t[i])
    if index[0].size != 0:
        tmp = out[index]
        tmp1 = outm[index]
        a = np.median(tmp) + np.sqrt(np.var(tmp))
        b = np.median(tmp) - np.sqrt(np.var(tmp))
        a1 = np.median(tmp1) + np.sqrt(np.var(tmp1))
        b1 = np.median(tmp1) - np.sqrt(np.var(tmp1))
        index0 = np.where( (b < tmp) &  (tmp < a) & (b1 < tmp1) &  (tmp1 < a1))
        index0 += np.min(index)
        Index = np.hstack((Index, index0.flatten()))
        U.append(np.mean(out[index0]))
        Um.append(np.mean(outm[index0]))
        T.append(t[i])

Index = np.array(Index, dtype=int)
outm = outm[Index]
out = out[Index]
tau = tau[Index]


fig, ax = plt.subplots()
l1 = ax.plot(tau, out, 'r.', label='Неусредненное')
l2 = ax.plot(tau, outm, 'b.', label="Усредненное")
ax.set_xlabel("Длительность $\\tau$, мс")
ax.set_ylabel("ОСШ")
legend = plt.legend(handles=[l1[0], l2[0]], loc=2)
plt.gca().add_artist(legend)

f = np.polyfit(tau, out, 1)
k = f[0]
f = np.poly1d(f)
fm = np.polyfit(tau, outm, 1)
km = fm[0]
fm = np.poly1d(fm)


# l3 = ax.plot(T, f(T), 'r', label="$k=%.1f$" % k)
# l4 = ax.plot(T, fm(T), 'b', label="$k=%.1f$" % km)


# legend = plt.legend(handles=[l3[0], l4[0]], loc=4)
# plt.gca().add_artist(legend)
fig.savefig("../imgs/task4/t4f1.pdf")


f = np.polyfit(T, U, 1)
k = f[0]
f = np.poly1d(f)
fm = np.polyfit(T, Um, 1)
km = fm[0]
fm = np.poly1d(fm)


fig, ax = plt.subplots()
# l1 = ax.plot(T, U, 'r.', label='Неусредненное')
l2 = ax.plot(T, Um, 'r.', label="Усредненное")

legend = plt.legend(handles=[l2[0]], loc=2)
plt.gca().add_artist(legend)


# l3 = ax.plot(T, f(T), 'r', label="$k=%.1f$" % k)
l4 = ax.plot(T, fm(T), 'b--', label="$k=%.1f$" % km)
legend = plt.legend(handles=[ l4[0]], loc=4)
plt.gca().add_artist(legend)
fig.savefig("../imgs/task4/t4f2.pdf")
# ax.legend()

# ax.set_xlabel("Длительность $\\tau$, мс")
# ax.set_ylabel("ОСШ")
# ax.legend


plt.show()