#### iterator

```
public static PrimitiveIterator.OfDouble iterator(Spliterator.OfDouble spliterator)
```
Creates an `PrimitiveIterator.OfDouble` from a
`Spliterator.OfDouble`.Traversal of elements should be accomplished through the iterator.
The behaviour of traversal is undefined if the spliterator is operated
after the iterator is returned.
Parameters:
`spliterator` - The spliterator
Returns:
An iterator
Throws:
`NullPointerException` - if the given spliterator is `null`




