#### isParallel

```
boolean isParallel()
```
Returns whether this stream, if a terminal operation were to be executed,
would execute in parallel. Calling this method after invoking an
terminal stream operation method may yield unpredictable results.
Returns:
`true` if this stream would execute in parallel if executed

