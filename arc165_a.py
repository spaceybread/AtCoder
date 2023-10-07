t = int(input())
i = 0

while i < t: 
  n = int(input())
  f = 2
  
  while n % f:
    f = f + 1
    if f**2 > n:
      f = n
  while n % f == 0: 
    n = n/f
    
  if n > 1:
    print('Yes')
  else:
    print('No')
  
  i = i + 1
