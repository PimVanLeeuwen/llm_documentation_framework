#### compareAndSetPendingCount

```
public final boolean compareAndSetPendingCount(int expected,
                                               int count)
```
Sets (atomically) the pending count to the given count only if
it currently holds the given expected value.
Parameters:
`expected` - the expected value
`count` - the new value
Returns:
`true` if successful

