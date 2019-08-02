def TransformTransform(A, N):
  b = []
  B = []
  S = 0
  k = 0
  m = 0
  summ = 0
  res = False
  if N == len(A):
    for i in range(N):
      for j in range(0, len(A) - i):
        k = i + j
        for z in range(j,k):
          if A[z] > m:
            m = A[z]
        b.append(m)
    for i in range(len(b)):
      for j in range(0, len(b) - i):
        k = i + j
        for z in range(j,k):
          if b[z] > m:
            m = b[z]
        B.append(m)
    for i in range(len(B)):
      summ = summ + B[i]
    if summ%2 == 0:
      res = True
      return res
  else:
    return 'Неверно введены данные!'