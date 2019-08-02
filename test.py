def Transform(A):
  b = []
  k = 0
  for i in range(len(A)):
    for j in range(0,len(A)-i):
      k = i + j
      m = 0
      for z in range(j,k+1):
        if m <= A[z]:
          m = A[z]
      b.append(m)
  return b

def TransformTransform(A, N):
  B = []
  summ = 0
  res = False
  B = Transform(A)
  print(len(B))
  B = Transform(B)
  print(len(B))
  for i in range(len(B)):
    summ = summ + B[i]
  print(summ)
  if summ%2 == 0 and summ > 0:
    res = True
  print(res)
  return res

#TransformTransform([1,2,3],3)
TransformTransform([1,2,1,7,2,4,3,1,5,1,2,1,6,1,2],15)