#### setDate

```
@Deprecated
public void setDate(int date)
```
Deprecated. As of JDK version 1.1,
replaced by `Calendar.set(Calendar.DAY_OF_MONTH, int date)`.
Sets the day of the month of this Date object to the
specified value. This Date object is modified so that
it represents a point in time within the specified day of the
month, with the year, month, hour, minute, and second the same
as before, as interpreted in the local time zone. If the date
was April 30, for example, and the date is set to 31, then it
will be treated as if it were on May 1, because April has only
30 days.
Parameters:
`date` - the day of the month value between 1-31.
See Also:
`Calendar`

