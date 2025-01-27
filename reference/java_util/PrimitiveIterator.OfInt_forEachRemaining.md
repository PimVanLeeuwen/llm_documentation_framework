#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Integer> action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Iterator<Integer>`
Implementation Requirements:
If the action is an instance of `IntConsumer` then it is cast
to `IntConsumer` and passed to `forEachRemaining(java.util.function.IntConsumer)`;
otherwise the action is adapted to an instance of
`IntConsumer`, by boxing the argument of `IntConsumer`,
and then passed to `forEachRemaining(java.util.function.IntConsumer)`.
Parameters:
`action` - The action to be performed for each element




