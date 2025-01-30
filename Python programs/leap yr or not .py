print("leapyear or not ")
year=int(input("enter the year :"))
if year%4==0 or year%100==0:
    print("it is an leap year")
elif year%400==0 :
    print("it is a leap year")
else:
    print("it is not a leap year")