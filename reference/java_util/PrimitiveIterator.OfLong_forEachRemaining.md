#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Long> action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Iterator<Long>`
Implementation Requirements:
If the action is an instance of `LongConsumer` then it is cast
to `LongConsumer` and passed to `forEachRemaining(java.util.function.LongConsumer)`;
otherwise the action is adapted to an instance of
`LongConsumer`, by boxing the argument of `LongConsumer`,
and then passed to `forEachRemaining(java.util.function.LongConsumer)`.
Parameters:
`action` - The action to be performed for each element




