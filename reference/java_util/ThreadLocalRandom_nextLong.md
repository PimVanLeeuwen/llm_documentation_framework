#### nextLong

```
public long nextLong(long origin,
                     long bound)
```
Returns a pseudorandom `long` value between the specified
origin (inclusive) and the specified bound (exclusive).
Parameters:
`origin` - the least value returned
`bound` - the upper bound (exclusive)
Returns:
a pseudorandom `long` value between the origin
(inclusive) and the bound (exclusive)
Throws:
`IllegalArgumentException` - if `origin` is greater than
or equal to `bound`

