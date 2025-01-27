#### stream

```
public static DoubleStream stream(double[] array,
                                  int startInclusive,
                                  int endExclusive)
```
Returns a sequential `DoubleStream` with the specified range of the
specified array as its source.
Parameters:
`array` - the array, assumed to be unmodified during use
`startInclusive` - the first index to cover, inclusive
`endExclusive` - index immediately past the last index to cover
Returns:
a `DoubleStream` for the array range
Throws:
`ArrayIndexOutOfBoundsException` - if `startInclusive` is
negative, `endExclusive` is less than
`startInclusive`, or `endExclusive` is greater than
the array size
Since:
1.8




