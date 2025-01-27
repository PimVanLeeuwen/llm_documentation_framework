#### getMaximum

```
public int getMaximum(int field)
```
Returns the maximum value for the given calendar field of this
`GregorianCalendar` instance. The maximum value is
defined as the largest value returned by the `get` method for any possible time value,
taking into consideration the current values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.
Specified by:
`getMaximum` in class `Calendar`
Parameters:
`field` - the calendar field.
Returns:
the maximum value for the given calendar field.
See Also:
`getMinimum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMinimum(int)`,
`getActualMaximum(int)`

