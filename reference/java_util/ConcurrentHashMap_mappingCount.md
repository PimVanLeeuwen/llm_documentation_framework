#### mappingCount

```
public long mappingCount()
```
Returns the number of mappings. This method should be used
instead of `size()` because a ConcurrentHashMap may
contain more mappings than can be represented as an int. The
value returned is an estimate; the actual count may differ if
there are concurrent insertions or removals.
Returns:
the number of mappings
Since:
1.8

