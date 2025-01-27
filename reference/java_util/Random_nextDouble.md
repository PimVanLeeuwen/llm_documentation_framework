#### nextDouble

```
public double nextDouble()
```
Returns the next pseudorandom, uniformly distributed
`double` value between `0.0` and
`1.0` from this random number generator's sequence.The general contract of `nextDouble` is that one
`double` value, chosen (approximately) uniformly from the
range `0.0d` (inclusive) to `1.0d` (exclusive), is
pseudorandomly generated and returned.The method `nextDouble` is implemented by class `Random`
as if by:
```
 
 public double nextDouble() {
   return (((long)next(26) << 27) + next(27))
     / (double)(1L << 53);
 }
```
The hedge "approximately" is used in the foregoing description only
because the `next` method is only approximately an unbiased
source of independently chosen bits. If it were a perfect source of
randomly chosen bits, then the algorithm shown would choose
`double` values from the stated range with perfect uniformity.[In early versions of Java, the result was incorrectly calculated as:
```
 
   return (((long)next(27) << 27) + next(27))
     / (double)(1L << 54);
```
This might seem to be equivalent, if not better, but in fact it
introduced a large nonuniformity because of the bias in the rounding
of floating-point numbers: it was three times as likely that the
low-order bit of the significand would be 0 than that it would be 1!
This nonuniformity probably doesn't matter much in practice, but we
strive for perfection.]
Returns:
the next pseudorandom, uniformly distributed `double`
value between `0.0` and `1.0` from this
random number generator's sequence
See Also:
`Math.random()`

