#python program to find average of the given elements in array
a=int(input("\n\n\t enter the size of array..."))
m=[]
sum=0
for i in range(0,a,1):
  x=int(input("\n\n\t enter the elements ..."))
  m.append(x)
print("\n\n\t the arrays are...",m)
for i in range(0,a,1):
  sum+=m[i]
  avg=sum/a
print("\n\n\t the avg elements of a given array is...",avg)