a=int(input('enter secend:'))
if a>0:
   hour=a//3600
   a=a%3600
   min=a//60
   sec=a%60
   print(hour,':',min,':',sec)
else :
   print('eror')
