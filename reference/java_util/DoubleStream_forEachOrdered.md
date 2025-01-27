#### forEachOrdered

```
void forEachOrdered(DoubleConsumer action)
```
Performs an action for each element of this stream, guaranteeing that
each element is processed in encounter order for streams that have a
defined encounter order.This is a terminal
operation.
Parameters:
`action` - a 
non-interfering action to perform on the elements
See Also:
`forEach(DoubleConsumer)`

