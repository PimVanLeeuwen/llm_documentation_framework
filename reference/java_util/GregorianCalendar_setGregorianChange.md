#### setGregorianChange

```
public void setGregorianChange(Date date)
```
Sets the `GregorianCalendar` change date. This is the point when the switch
from Julian dates to Gregorian dates occurred. Default is October 15,
1582 (Gregorian). Previous to this, dates will be in the Julian calendar.To obtain a pure Julian calendar, set the change date to
`Date(Long.MAX_VALUE)`. To obtain a pure Gregorian calendar,
set the change date to `Date(Long.MIN_VALUE)`.
Parameters:
`date` - the given Gregorian cutover date.

