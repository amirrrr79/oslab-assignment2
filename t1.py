import math
while True:
    print('sum')
    print('mines')
    print('multiply')
    print('divideed')
    print('sin')
    print('cos')
    print('tan')
    print('cot')
    print('log')

    i=(input('Enter= '))

    if i=='sum':
        adad1=int(input('adad1= '))
        adad2=int(input('adad2= '))
        c=adad1+adad2
        print('sum= ',c)
    if i=='mines':
        adad1=int(input('adad1= '))
        adad2=int(input('adad2= '))
        c=adad1-adad2
        print('mines= ')
    if i=='multiply':
        adad1=int(input('adad1= '))
        adad2=int(input('adad2= '))
        c=adad1*adad2
        print('multiply= ',c)
    if i=='divided':
        adad1=int(input('adad1= '))
        adad2=int(input('adad2= ')) 
        c=adad1/adad2 
        print('divided= ',c)
    if i=='sin':
       zaviye=float(input('zaviye= ')) 
       daraje= zaviye/360*2*math.pi
       c=math.sin(daraje)
       print('sin= ',c)
    if i=='cos':
        zaviye=float(input('zaviye= ')) 
        daraje= zaviye/360*2*math.pi
        c=math.cos(daraje)
        print('cos= ',c)
    if i=='tan':
        zaviye=float(input('zaviye= ')) 
        daraje= zaviye/360*2*math.pi
        c=math.tan(daraje)
        print('tan= ',c)
    if i=='cot':
        zaviye=float(input('zaviye= ')) 
        daraje= zaviye/360*2*math.pi
        c=1/math.tan(daraje)
        print('cot= ',c)
    if i=='log':
        a=int(input('a= '))
        c=math.log(a)  
        print('log= ',c)  
        break    


            

