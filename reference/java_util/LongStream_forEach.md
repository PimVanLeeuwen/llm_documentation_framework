#### forEach

```
void forEach(LongConsumer action)
```
Performs an action for each element of this stream.This is a terminal
operation.For parallel stream pipelines, this operation does not
guarantee to respect the encounter order of the stream, as doing so
would sacrifice the benefit of parallelism. For any given element, the
action may be performed at whatever time and in whatever thread the
library chooses. If the action accesses shared state, it is
responsible for providing the required synchronization.
Parameters:
`action` - a 
non-interfering action to perform on the elements

