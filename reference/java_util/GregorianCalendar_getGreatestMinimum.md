#### getGreatestMinimum

```
public int getGreatestMinimum(int field)
```
Returns the highest minimum value for the given calendar field
of this `GregorianCalendar` instance. The highest
minimum value is defined as the largest value returned by
`getActualMinimum(int)` for any possible time value,
taking into consideration the current values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.
Specified by:
`getGreatestMinimum` in class `Calendar`
Parameters:
`field` - the calendar field.
Returns:
the highest minimum value for the given calendar field.
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getLeastMaximum(int)`,
`getActualMinimum(int)`,
`getActualMaximum(int)`

