#### filter

```
DoubleStream filter(DoublePredicate predicate)
```
Returns a stream consisting of the elements of this stream that match
the given predicate.This is an intermediate
operation.
Parameters:
`predicate` - a non-interfering,
stateless
predicate to apply to each element to determine if it
should be included
Returns:
the new stream

