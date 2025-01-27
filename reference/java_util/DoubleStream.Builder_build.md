#### build

```
DoubleStream build()
```
Builds the stream, transitioning this builder to the built state.
An `IllegalStateException` is thrown if there are further
attempts to operate on the builder after it has entered the built
state.
Returns:
the built stream
Throws:
`IllegalStateException` - if the builder has already transitioned
to the built state




