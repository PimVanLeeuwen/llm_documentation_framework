#### setInstant

```
public Calendar.Builder setInstant(Date instant)
```
Sets the instant parameter to the `instant` value given by a
`Date`. This method is equivalent to a call to
`setInstant(instant.getTime())`.
Parameters:
`instant` - a `Date` representing a millisecond offset from
the Epoch
Returns:
this `Calendar.Builder`
Throws:
`NullPointerException` - if `instant` is `null`
`IllegalStateException` - if any of the field parameters have
already been set
See Also:
`Calendar.setTime(Date)`,
`Calendar.setTimeInMillis(long)`,
`Calendar.time`

