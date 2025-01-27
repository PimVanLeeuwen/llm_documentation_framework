#### nextDouble

```
public double nextDouble(double origin,
                         double bound)
```
Returns a pseudorandom `double` value between the specified
origin (inclusive) and bound (exclusive).
Parameters:
`origin` - the least value returned
`bound` - the upper bound (exclusive)
Returns:
a pseudorandom `double` value between the origin
(inclusive) and the bound (exclusive)
Throws:
`IllegalArgumentException` - if `origin` is greater than
or equal to `bound`

