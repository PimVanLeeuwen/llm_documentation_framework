#### mapToObj

```
<U> Stream<U> mapToObj(DoubleFunction<? extends U> mapper)
```
Returns an object-valued `Stream` consisting of the results of
applying the given function to the elements of this stream.This is an 
intermediate operation.
Type Parameters:
`U` - the element type of the new stream
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element
Returns:
the new stream

