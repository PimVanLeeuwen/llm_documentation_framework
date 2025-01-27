#### nextInt

```
public int nextInt(int bound)
```
Returns a pseudorandom, uniformly distributed `int` value
between 0 (inclusive) and the specified value (exclusive), drawn from
this random number generator's sequence. The general contract of
`nextInt` is that one `int` value in the specified range
is pseudorandomly generated and returned. All `bound` possible
`int` values are produced with (approximately) equal
probability. The method `nextInt(int bound)` is implemented by
class `Random` as if by:
```
 
 public int nextInt(int bound) {
   if (bound <= 0)
     throw new IllegalArgumentException("bound must be positive");

   if ((bound & -bound) == bound)  // i.e., bound is a power of 2
     return (int)((bound * (long)next(31)) >> 31);

   int bits, val;
   do {
       bits = next(31);
       val = bits % bound;
   } while (bits - val + (bound-1) < 0);
   return val;
 }
```
The hedge "approximately" is used in the foregoing description only
because the next method is only approximately an unbiased source of
independently chosen bits. If it were a perfect source of randomly
chosen bits, then the algorithm shown would choose `int`
values from the stated range with perfect uniformity.The algorithm is slightly tricky. It rejects values that would result
in an uneven distribution (due to the fact that 2^31 is not divisible
by n). The probability of a value being rejected depends on n. The
worst case is n=2^30+1, for which the probability of a reject is 1/2,
and the expected number of iterations before the loop terminates is 2.The algorithm treats the case where n is a power of two specially: it
returns the correct number of high-order bits from the underlying
pseudo-random number generator. In the absence of special treatment,
the correct number of low-order bits would be returned. Linear
congruential pseudo-random number generators such as the one
implemented by this class are known to have short periods in the
sequence of values of their low-order bits. Thus, this special case
greatly increases the length of the sequence of values returned by
successive calls to this method if n is a small power of two.
Parameters:
`bound` - the upper bound (exclusive). Must be positive.
Returns:
the next pseudorandom, uniformly distributed `int`
value between zero (inclusive) and `bound` (exclusive)
from this random number generator's sequence
Throws:
`IllegalArgumentException` - if bound is not positive
Since:
1.2

