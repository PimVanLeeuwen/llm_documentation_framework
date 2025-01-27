#### map

```
<R> Stream<R> map(Function<? super T,? extends R> mapper)
```
Returns a stream consisting of the results of applying the given
function to the elements of this stream.This is an intermediate
operation.
Type Parameters:
`R` - The element type of the new stream
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element
Returns:
the new stream

