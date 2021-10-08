# A000127
[OEIS](https://oeis.org/) sequence [A000127](https://oeis.org/A000127) is as follows: `1, 2, 4, 8, 16, 31, 57, 99, 163, 256, 386`. It resembles powers of two early on, but doesn't line up with them well. See [this video](https://www.youtube.com/watch?v=4AuV93LOPcE) for an explanation of the sequence and the math that generates it. Below is an explanation of my code, assuming you already understand the math somewhat.

## Line by line...
```python
print((a := δΣ_λ(4,1))) # all nums
```
`:=` is the [assignment expression operator](https://www.python.org/dev/peps/pep-0572/), which sets `a` to the return value of `δΣ_λ(4,1)` and evaluates to that return value. For example, 
```python
if (v := True):
 # ...
```
... will always resolve to `True`.

---

```python
print(list(filter(lambda i: log2(i)*10%10==0, a))) # only powers of two
```

This will print us the list of numbers in `a` which are powers of 2. Most of the code is a simple filter, but the formula `log2(n)*10%10==0` will always return `True` if `n` is a power of two. 

For example, let's assume `n=32`:
1. First, compute `log2(n) = 5.0`. For all powers of two, this will be a whole number with no decimals.
2. Then, assert that this value is a whole number with `log2(n)*10%10`, which will give us the ones-place digit of `log2(n)` times 10. For powers of two, this is always zero.

---

```python
def δΣ_λ(a: int, i: int, *, carry = [1]*100) -> list[int]:
 if a == 0:
  return carry
 else:
  return δΣ_λ(a-1,i,carry=δΣ(i,carry))
```
This is a recursive function. Effectively, its whole purpose is to compute `δΣ(a,v)` repeatedly and return the result. 

Before explaining the function cases, note that the function signature:

```python
def δΣ_λ(a: int, i: int, *, carry = [1]*100) -> list[int]
```

... uses the special argument `*`. This just requires that all arguments after it be named fully in function calls. So, to change carry, you would have to run e.g. `δΣ_λ(a=a,i=i,carry=[1,2,3,4,5])`.

```python
if a == 0:
 return carry
```

This is its base case. It will always return the value of `carry`, which is initialized to a list of a million ones. So, `δΣ_λ(0,1)` will always return `[1,1,1,...]` and so on.

```python
else:
 return δΣ_λ(a-1,i,carry=δΣ(i,carry))
```

This is its recursive case. This will call itself again (decrementing `a` so it will eventually end) with carry set to `δΣ(i,carry)`, meaning that the result of `a`-many applications of `δΣ` is our ultimate return value.

---

```python
def δΣ(a: int, Δ: list[int]) -> list[int]:
 res=[a]
 for ri,vi in zip(res,Δ):
  res.append(ri+vi)
 return res
```

`δΣ` takes two inputs: An initializer variable `a` and a list of differences `Δ`. 

This function is very simple. To see what it's doing, look at what an application of `zip()` does:
```python
>>> a = [1,2,3]
>>> b = [2,4,6]
>>> list(zip(a,b)) = [(1,2), (2,4), (3,6)]
```

All that's done with this is e.g. `(1,2)` is summed to produce `3`, or `(2,4)` to produce `6`. This completes the functionality necessary to represent `A000127`.