def Transform(A):
  b = []
  m = 0
  for i in range(len(A)):
      for j in range(0, len(A) - i - 1):
        k = i + j
        for z in range(j,k):
          if A[z] > m:
            m = A[z]
        b.append(m)
  return b
def TransformTransform(A, N):
  B = []
  summ = 0
  res = False
  if N == len(A):
    B = Transform(A)
    B = Transform(B)
    for i in range(len(B)):
      summ = summ + B[i]
    if summ%2 == 0:
      res = True
      return res
  else:
    return 'Неверно введены данные!'