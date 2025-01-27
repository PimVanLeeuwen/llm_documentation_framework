#### forEachRemaining

```
default void forEachRemaining(Consumer<? super Long> action)
```
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is `Spliterator.ORDERED`, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.
Specified by:
`forEachRemaining` in interface `Spliterator<Long>`
Implementation Requirements:
If the action is an instance of `LongConsumer` then it is cast
to `LongConsumer` and passed to
`forEachRemaining(java.util.function.LongConsumer)`; otherwise
the action is adapted to an instance of `LongConsumer`, by
boxing the argument of `LongConsumer`, and then passed to
`forEachRemaining(java.util.function.LongConsumer)`.
Parameters:
`action` - The action




