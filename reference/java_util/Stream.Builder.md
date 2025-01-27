```
public static interface Stream.Builder<T>
extends Consumer<T>
```
A mutable builder for a `Stream`. This allows the creation of a
`Stream` by generating elements individually and adding them to the
`Builder` (without the copying overhead that comes from using
an `ArrayList` as a temporary buffer.)A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
when the `build()` method is called, which creates an ordered
`Stream` whose elements are the elements that were added to the stream
builder, in the order they were added.
Since:
1.8
See Also:
`Stream.builder()`
