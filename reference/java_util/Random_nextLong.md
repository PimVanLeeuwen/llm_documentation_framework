#### nextLong

```
public long nextLong()
```
Returns the next pseudorandom, uniformly distributed `long`
value from this random number generator's sequence. The general
contract of `nextLong` is that one `long` value is
pseudorandomly generated and returned.The method `nextLong` is implemented by class `Random`
as if by:
```
 
 public long nextLong() {
   return ((long)next(32) << 32) + next(32);
 }
```
Because class `Random` uses a seed with only 48 bits,
this algorithm will not return all possible `long` values.
Returns:
the next pseudorandom, uniformly distributed `long`
value from this random number generator's sequence

