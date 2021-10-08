from math import log2

def δΣ(a: int, Δ: list[int]) -> list[int]:
 res=[a]
 for ri,vi in zip(res,Δ):
  res.append(ri+vi)
 return res

def δΣ_λ(a: int, i: int, *, carry = [1]*100) -> list[int]:
 if a == 0:
  return carry
 else:
  return δΣ_λ(a-1,i,carry=δΣ(i,carry))

if __name__ == '__main__':
 print((a := δΣ_λ(4,1))) # all nums
 print(list(filter(lambda i: log2(i)*10%10==0, a))) # only powers of two