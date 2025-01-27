#### getMinimum

```
public abstract int getMinimum(int field)
```
Returns the minimum value for the given calendar field of this
`Calendar` instance. The minimum value is defined as
the smallest value returned by the `get` method
for any possible time value. The minimum value depends on
calendar system specific parameters of the instance.
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

