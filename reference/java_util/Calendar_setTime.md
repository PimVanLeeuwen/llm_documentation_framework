#### setTime

```
public final void setTime(Date date)
```
Sets this Calendar's time with the given `Date`.Note: Calling `setTime()` with
`Date(Long.MAX_VALUE)` or `Date(Long.MIN_VALUE)`
may yield incorrect field values from `get()`.
Parameters:
`date` - the given Date.
See Also:
`getTime()`,
`setTimeInMillis(long)`

