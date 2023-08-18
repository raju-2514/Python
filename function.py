#no argument
def fun1():
    print("function1")

#Two argument 
def function1(x,y):
  return (x, y)
def function3(x):
   return x+x+x;

#For loop in funciton
def power(num,x=1):
   result=1
   for i in range(x):
     result=result*num
   return result

#print the value of all column
# fun1()
# print("the value of all data with adding :",function1(5,6))
# print("the ",function3(9))    

print(power(5))
print(power(2,3))
