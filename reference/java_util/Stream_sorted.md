#### sorted

```
Stream<T> sorted(Comparator<? super T> comparator)
```
Returns a stream consisting of the elements of this stream, sorted
according to the provided `Comparator`.For ordered streams, the sort is stable. For unordered streams, no
stability guarantees are made.This is a stateful
intermediate operation.
Parameters:
`comparator` - a non-interfering,
stateless
`Comparator` to be used to compare stream elements
Returns:
the new stream

