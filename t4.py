hour=int(input('hour:'))
min=int(input('min:'))
sec=int(input('sec:'))

if hour>0 and 0<=min<60 and sec>=0:
   s=hour*3600+min*60+sec
   print(s)
else:          
  print('false')    