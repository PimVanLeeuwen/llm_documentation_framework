#### emptyIntSpliterator

```
public static Spliterator.OfInt emptyIntSpliterator()
```
Creates an empty `Spliterator.OfInt`The empty spliterator reports `Spliterator.SIZED` and
`Spliterator.SUBSIZED`. Calls to
`Spliterator.trySplit()` always return `null`.
Returns:
An empty spliterator

