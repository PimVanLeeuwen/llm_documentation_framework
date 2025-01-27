#### max

```
Optional<T> max(Comparator<? super T> comparator)
```
Returns the maximum element of this stream according to the provided
`Comparator`. This is a special case of a
reduction.This is a terminal
operation.
Parameters:
`comparator` - a non-interfering,
stateless
`Comparator` to compare elements of this stream
Returns:
an `Optional` describing the maximum element of this stream,
or an empty `Optional` if the stream is empty
Throws:
`NullPointerException` - if the maximum element is null

