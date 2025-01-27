#### getLeastMaximum

```
public int getLeastMaximum(int field)
```
Returns the lowest maximum value for the given calendar field
of this `GregorianCalendar` instance. The lowest
maximum value is defined as the smallest value returned by
`getActualMaximum(int)` for any possible time value,
taking into consideration the current values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.
Specified by:
`getLeastMaximum` in class `Calendar`
Parameters:
`field` - the calendar field
Returns:
the lowest maximum value for the given calendar field.
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getActualMinimum(int)`,
`getActualMaximum(int)`

