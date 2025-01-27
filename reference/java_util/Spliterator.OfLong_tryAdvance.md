#### tryAdvance

```
default boolean tryAdvance(Consumer<? super Long> action)
```
If a remaining element exists, performs the given action on it,
returning `true`; else returns `false`. If this
Spliterator is `Spliterator.ORDERED` the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.
Specified by:
`tryAdvance` in interface `Spliterator<Long>`
Implementation Requirements:
If the action is an instance of `LongConsumer` then it is cast
to `LongConsumer` and passed to
`tryAdvance(java.util.function.LongConsumer)`; otherwise
the action is adapted to an instance of `LongConsumer`, by
boxing the argument of `LongConsumer`, and then passed to
`tryAdvance(java.util.function.LongConsumer)`.
Parameters:
`action` - The action
Returns:
`false` if no remaining elements existed
upon entry to this method, else `true`.

