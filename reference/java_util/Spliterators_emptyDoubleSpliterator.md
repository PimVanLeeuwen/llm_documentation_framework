#### emptyDoubleSpliterator

```
public static Spliterator.OfDouble emptyDoubleSpliterator()
```
Creates an empty `Spliterator.OfDouble`The empty spliterator reports `Spliterator.SIZED` and
`Spliterator.SUBSIZED`. Calls to
`Spliterator.trySplit()` always return `null`.
Returns:
An empty spliterator

