```
public abstract static class Spliterators.AbstractIntSpliterator
extends Object
implements Spliterator.OfInt
```
An abstract `Spliterator.OfInt` that implements `trySplit` to
permit limited parallelism.To implement a spliterator an extending class need only
implement `Spliterator.OfInt.tryAdvance(java.util.function.IntConsumer)`
tryAdvance}. The extending class should override
`Spliterator.OfInt.forEachRemaining(java.util.function.IntConsumer)` forEach} if it
can provide a more performant implementation.
API Note:
This class is a useful aid for creating a spliterator when it is not
possible or difficult to efficiently partition elements in a manner
allowing balanced parallel computation.An alternative to using this class, that also permits limited
parallelism, is to create a spliterator from an iterator
(see `Spliterators.spliterator(java.util.PrimitiveIterator.OfInt, long, int)`.
Depending on the circumstances using an iterator may be easier or more
convenient than extending this class. For example, if there is already an
iterator available to use then there is no need to extend this class.
Since:
1.8
See Also:
`Spliterators.spliterator(java.util.PrimitiveIterator.OfInt, long, int)`
