#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Double> action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Iterator<Double>`
Implementation Requirements:
If the action is an instance of `DoubleConsumer` then it is
cast to `DoubleConsumer` and passed to
`forEachRemaining(java.util.function.DoubleConsumer)`; otherwise the action is adapted to
an instance of `DoubleConsumer`, by boxing the argument of
`DoubleConsumer`, and then passed to
`forEachRemaining(java.util.function.DoubleConsumer)`.
Parameters:
`action` - The action to be performed for each element




