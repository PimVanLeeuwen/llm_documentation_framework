#### doubles

```
public DoubleStream doubles(double randomNumberOrigin,
                            double randomNumberBound)
```
Returns an effectively unlimited stream of pseudorandom `double` values, each conforming to the given origin (inclusive) and bound
(exclusive).
Overrides:
`doubles` in class `Random`
Implementation Note:
This method is implemented to be equivalent to `doubles(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)`.
Parameters:
`randomNumberOrigin` - the origin (inclusive) of each random value
`randomNumberBound` - the bound (exclusive) of each random value
Returns:
a stream of pseudorandom `double` values,
each with the given origin (inclusive) and bound (exclusive)
Throws:
`IllegalArgumentException` - if `randomNumberOrigin`
is greater than or equal to `randomNumberBound`
Since:
1.8




