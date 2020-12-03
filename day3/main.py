
results = []

def test(i,double):
  hits=0
  x = 0
  f = open("input", "r")
  line = f.readline()

  while line:
    if line[x] == '#':
      hits+=1
    x+=i


    if x >= len(line)-1:
      x=x+1-len(line)
    line = f.readline()
    if double and line:
      line = f.readline()
  return hits

for i in range(1,9,2):
  results.append(test(i,False))

results.append(test(1,True))
sum = 1
for q in results:
  sum*=q
print(sum)
