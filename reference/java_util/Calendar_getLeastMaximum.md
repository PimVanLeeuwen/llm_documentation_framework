#### getLeastMaximum

```
public abstract int getLeastMaximum(int field)
```
Returns the lowest maximum value for the given calendar field
of this `Calendar` instance. The lowest maximum
value is defined as the smallest value returned by `getActualMaximum(int)` for any possible time value. The least
maximum value depends on calendar system specific parameters of
the instance. For example, a `Calendar` for the
Gregorian calendar system returns 28 for the
`DAY_OF_MONTH` field, because the 28th is the last
day of the shortest month of this calendar, February in a
common year.
Parameters:
`field` - the calendar field.
Returns:
the lowest maximum value for the given calendar field.
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getActualMinimum(int)`,
`getActualMaximum(int)`

