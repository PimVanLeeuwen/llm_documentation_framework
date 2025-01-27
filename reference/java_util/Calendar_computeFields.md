#### computeFields

```
protected abstract void computeFields()
```
Converts the current millisecond time value `time`
to calendar field values in `fields[]`.
This allows you to sync up the calendar field values with
a new time that is set for the calendar. The time is not
recomputed first; to recompute the time, then the fields, call the
`complete()` method.
See Also:
`computeTime()`

