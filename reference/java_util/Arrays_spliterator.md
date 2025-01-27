#### spliterator

```
public static Spliterator.OfDouble spliterator(double[] array,
                                               int startInclusive,
                                               int endExclusive)
```
Returns a `Spliterator.OfDouble` covering the specified range of
the specified array.The spliterator reports `Spliterator.SIZED`,
`Spliterator.SUBSIZED`, `Spliterator.ORDERED`, and
`Spliterator.IMMUTABLE`.
Parameters:
`array` - the array, assumed to be unmodified during use
`startInclusive` - the first index to cover, inclusive
`endExclusive` - index immediately past the last index to cover
Returns:
a spliterator for the array elements
Throws:
`ArrayIndexOutOfBoundsException` - if `startInclusive` is
negative, `endExclusive` is less than
`startInclusive`, or `endExclusive` is greater than
the array size
Since:
1.8

