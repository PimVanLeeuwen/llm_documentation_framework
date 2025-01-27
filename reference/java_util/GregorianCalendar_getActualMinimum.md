#### getActualMinimum

```
public int getActualMinimum(int field)
```
Returns the minimum value that this calendar field could have,
taking into consideration the given time value and the current
values of the
`getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek`,
`getGregorianChange` and
`getTimeZone` methods.For example, if the Gregorian change date is January 10,
1970 and the date of this `GregorianCalendar` is
January 20, 1970, the actual minimum value of the
`DAY_OF_MONTH` field is 10 because the previous date
of January 10, 1970 is December 27, 1996 (in the Julian
calendar). Therefore, December 28, 1969 to January 9, 1970
don't exist.
Overrides:
`getActualMinimum` in class `Calendar`
Parameters:
`field` - the calendar field
Returns:
the minimum of the given field for the time value of
this `GregorianCalendar`
Since:
1.2
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMaximum(int)`

