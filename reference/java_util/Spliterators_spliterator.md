#### spliterator

```
public static Spliterator.OfDouble spliterator(PrimitiveIterator.OfDouble iterator,
                                               long size,
                                               int characteristics)
```
Creates a `Spliterator.OfDouble` using a given
`DoubleStream.DoubleIterator` as the source of elements, and with a
given initially reported size.The spliterator is not
late-binding, inherits
the fail-fast properties of the iterator, and implements
`trySplit` to permit limited parallelism.Traversal of elements should be accomplished through the spliterator.
The behaviour of splitting and traversal is undefined if the iterator is
operated on after the spliterator is returned, or the initially reported
size is not equal to the actual number of elements in the source.
Parameters:
`iterator` - The iterator for the source
`size` - The number of elements in the source, to be reported as
initial `estimateSize`
`characteristics` - Characteristics of this spliterator's source or
elements. The characteristics `SIZED` and `SUBSIZED`
are additionally reported unless `CONCURRENT` is supplied.
Returns:
A spliterator from an iterator
Throws:
`NullPointerException` - if the given iterator is `null`

