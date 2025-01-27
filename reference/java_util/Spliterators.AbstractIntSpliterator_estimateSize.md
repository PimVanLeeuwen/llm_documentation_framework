#### estimateSize

```
public long estimateSize()
```
Returns an estimate of the number of elements that would be
encountered by a `Spliterator.forEachRemaining(java.util.function.Consumer<? super T>)` traversal, or returns `Long.MAX_VALUE` if infinite, unknown, or too expensive to compute.If this Spliterator is `Spliterator.SIZED` and has not yet been partially
traversed or split, or this Spliterator is `Spliterator.SUBSIZED` and has
not yet been partially traversed, this estimate must be an accurate
count of elements that would be encountered by a complete traversal.
Otherwise, this estimate may be arbitrarily inaccurate, but must decrease
as specified across invocations of `Spliterator.trySplit()`.
Specified by:
`estimateSize` in interface `Spliterator<Integer>`
Implementation Requirements:
This implementation returns the estimated size as reported when
created and, if the estimate size is known, decreases in size when
split.
Returns:
the estimated size, or `Long.MAX_VALUE` if infinite,
unknown, or too expensive to compute.

