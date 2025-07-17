n=int(input("Choose n"))
f_n=0
f_n_1=1
if n==0:
    print(0)
if n==1:
    print(1)
for i in range(n-1):
    f_n_2=f_n_1+f_n
    f_n=f_n_1
    f_n_1=f_n_2
print(f_n_2)
