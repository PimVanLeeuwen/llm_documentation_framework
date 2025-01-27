#### emptyLongSpliterator

```
public static Spliterator.OfLong emptyLongSpliterator()
```
Creates an empty `Spliterator.OfLong`The empty spliterator reports `Spliterator.SIZED` and
`Spliterator.SUBSIZED`. Calls to
`Spliterator.trySplit()` always return `null`.
Returns:
An empty spliterator

