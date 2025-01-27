#### nextBoolean

```
public boolean nextBoolean()
```
Returns the next pseudorandom, uniformly distributed
`boolean` value from this random number generator's
sequence. The general contract of `nextBoolean` is that one
`boolean` value is pseudorandomly generated and returned. The
values `true` and `false` are produced with
(approximately) equal probability.The method `nextBoolean` is implemented by class `Random`
as if by:
```
 
 public boolean nextBoolean() {
   return next(1) != 0;
 }
```

Returns:
the next pseudorandom, uniformly distributed
`boolean` value from this random number generator's
sequence
Since:
1.2

