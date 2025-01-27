#### nextFloat

```
public float nextFloat()
```
Returns the next pseudorandom, uniformly distributed `float`
value between `0.0` and `1.0` from this random
number generator's sequence.The general contract of `nextFloat` is that one
`float` value, chosen (approximately) uniformly from the
range `0.0f` (inclusive) to `1.0f` (exclusive), is
pseudorandomly generated and returned. All 224 possible
`float` values of the form m x 2-24,
where m is a positive integer less than 224, are
produced with (approximately) equal probability.The method `nextFloat` is implemented by class `Random`
as if by:
```
 
 public float nextFloat() {
   return next(24) / ((float)(1 << 24));
 }
```
The hedge "approximately" is used in the foregoing description only
because the next method is only approximately an unbiased source of
independently chosen bits. If it were a perfect source of randomly
chosen bits, then the algorithm shown would choose `float`
values from the stated range with perfect uniformity.[In early versions of Java, the result was incorrectly calculated as:
```
 
   return next(30) / ((float)(1 << 30));
```
This might seem to be equivalent, if not better, but in fact it
introduced a slight nonuniformity because of the bias in the rounding
of floating-point numbers: it was slightly more likely that the
low-order bit of the significand would be 0 than that it would be 1.]
Returns:
the next pseudorandom, uniformly distributed `float`
value between `0.0` and `1.0` from this
random number generator's sequence

