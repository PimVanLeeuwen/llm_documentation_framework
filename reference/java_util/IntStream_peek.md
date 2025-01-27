#### peek

```
IntStream peek(IntConsumer action)
```
Returns a stream consisting of the elements of this stream, additionally
performing the provided action on each element as elements are consumed
from the resulting stream.This is an intermediate
operation.For parallel stream pipelines, the action may be called at
whatever time and in whatever thread the element is made available by the
upstream operation. If the action modifies shared state,
it is responsible for providing the required synchronization.
API Note:
This method exists mainly to support debugging, where you want
to see the elements as they flow past a certain point in a pipeline:
```

     IntStream.of(1, 2, 3, 4)
         .filter(e -> e > 2)
         .peek(e -> System.out.println("Filtered value: " + e))
         .map(e -> e * e)
         .peek(e -> System.out.println("Mapped value: " + e))
         .sum();
 
```

Parameters:
`action` - a 
non-interfering action to perform on the elements as
they are consumed from the stream
Returns:
the new stream

