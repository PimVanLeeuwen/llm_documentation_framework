#### spliteratorUnknownSize

```
public static Spliterator.OfDouble spliteratorUnknownSize(PrimitiveIterator.OfDouble iterator,
                                                          int characteristics)
```
Creates a `Spliterator.OfDouble` using a given
`DoubleStream.DoubleIterator` as the source of elements, with no
initial size estimate.The spliterator is not
late-binding, inherits
the fail-fast properties of the iterator, and implements
`trySplit` to permit limited parallelism.Traversal of elements should be accomplished through the spliterator.
The behaviour of splitting and traversal is undefined if the iterator is
operated on after the spliterator is returned.
Parameters:
`iterator` - The iterator for the source
`characteristics` - Characteristics of this spliterator's source
or elements (`SIZED` and `SUBSIZED`, if supplied, are
ignored and are not reported.)
Returns:
A spliterator from an iterator
Throws:
`NullPointerException` - if the given iterator is `null`

