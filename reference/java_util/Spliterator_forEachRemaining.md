#### forEachRemaining

```
default void forEachRemaining(Consumer<? super T> action)
```
Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is `ORDERED`, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.
Implementation Requirements:
The default implementation repeatedly invokes `tryAdvance(java.util.function.Consumer<? super T>)` until
it returns `false`. It should be overridden whenever possible.
Parameters:
`action` - The action
Throws:
`NullPointerException` - if the specified action is null

