```
public static interface DoubleStream.Builder
extends DoubleConsumer
```
A mutable builder for a `DoubleStream`.A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
begins when the `build()` method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.
Since:
1.8
See Also:
`DoubleStream.builder()`
