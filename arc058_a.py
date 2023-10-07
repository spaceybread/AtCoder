def check(strN, digits, digC):
  i = 0
  while i < digC:
    if digits[i] in strN:
      return False
    i = i + 1
    
  return True
  
linein = input().split()
n = linein[0]
k = int(linein[1])

dig = input().split()

while True:
  if check(n, dig, k):
    print(n)
    quit()
  else:
    n = str(int(n) + 1)

  
