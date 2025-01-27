#### emptySpliterator

```
public static <T> Spliterator<T> emptySpliterator()
```
Creates an empty `Spliterator`The empty spliterator reports `Spliterator.SIZED` and
`Spliterator.SUBSIZED`. Calls to
`Spliterator.trySplit()` always return `null`.
Type Parameters:
`T` - Type of elements
Returns:
An empty spliterator

