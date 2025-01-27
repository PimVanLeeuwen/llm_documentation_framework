#### mapToInt

```
IntStream mapToInt(LongToIntFunction mapper)
```
Returns an `IntStream` consisting of the results of applying the
given function to the elements of this stream.This is an intermediate
operation.
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element
Returns:
the new stream

