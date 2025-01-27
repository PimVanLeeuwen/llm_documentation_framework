#### getGreatestMinimum

```
public abstract int getGreatestMinimum(int field)
```
Returns the highest minimum value for the given calendar field
of this `Calendar` instance. The highest minimum
value is defined as the largest value returned by `getActualMinimum(int)` for any possible time value. The
greatest minimum value depends on calendar system specific
parameters of the instance.
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

