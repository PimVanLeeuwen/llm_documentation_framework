#### forEachRemaining

```
default void forEachRemaining(T_CONS action)
```
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is `Spliterator.ORDERED`,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.
Implementation Requirements:
The default implementation repeatedly invokes `tryAdvance(T_CONS)`
until it returns `false`. It should be overridden whenever
possible.
Parameters:
`action` - The action
Throws:
`NullPointerException` - if the specified action is null




