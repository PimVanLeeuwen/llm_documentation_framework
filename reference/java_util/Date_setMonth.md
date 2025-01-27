#### setMonth

```
@Deprecated
public void setMonth(int month)
```
Deprecated. As of JDK version 1.1,
replaced by `Calendar.set(Calendar.MONTH, int month)`.
Sets the month of this date to the specified value. This
Date object is modified so that it represents a point
in time within the specified month, with the year, date, hour,
minute, and second the same as before, as interpreted in the
local time zone. If the date was October 31, for example, and
the month is set to June, then the new date will be treated as
if it were on July 1, because June has only 30 days.
Parameters:
`month` - the month value between 0-11.
See Also:
`Calendar`

