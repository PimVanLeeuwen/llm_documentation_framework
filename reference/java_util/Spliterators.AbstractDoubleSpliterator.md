```
public abstract static class Spliterators.AbstractDoubleSpliterator
extends Object
implements Spliterator.OfDouble
```
An abstract `Spliterator.OfDouble` that implements
`trySplit` to permit limited parallelism.To implement a spliterator an extending class need only
implement `Spliterator.OfDouble.tryAdvance(java.util.function.DoubleConsumer)`
tryAdvance}. The extending class should override
`Spliterator.OfDouble.forEachRemaining(java.util.function.DoubleConsumer)` forEach} if
it can provide a more performant implementation.
API Note:
This class is a useful aid for creating a spliterator when it is not
possible or difficult to efficiently partition elements in a manner
allowing balanced parallel computation.An alternative to using this class, that also permits limited
parallelism, is to create a spliterator from an iterator
(see `Spliterators.spliterator(java.util.PrimitiveIterator.OfDouble, long, int)`.
Depending on the circumstances using an iterator may be easier or more
convenient than extending this class. For example, if there is already an
iterator available to use then there is no need to extend this class.
Since:
1.8
See Also:
`Spliterators.spliterator(java.util.PrimitiveIterator.OfDouble, long, int)`
