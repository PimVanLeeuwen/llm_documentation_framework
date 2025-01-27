#### getMinimum

```
public int getMinimum(int field)
```
Returns the minimum value for the given calendar field of this
`GregorianCalendar` instance. The minimum value is
defined as the smallest value returned by the `get` method for any possible time value,
taking into consideration the current values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.
Specified by:
`getMinimum` in class `Calendar`
Parameters:
`field` - the calendar field.
Returns:
the minimum value for the given calendar field.
See Also:
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMinimum(int)`,
`getActualMaximum(int)`

