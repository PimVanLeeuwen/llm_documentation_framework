#### getMaximum

```
public abstract int getMaximum(int field)
```
Returns the maximum value for the given calendar field of this
`Calendar` instance. The maximum value is defined as
the largest value returned by the `get` method
for any possible time value. The maximum value depends on
calendar system specific parameters of the instance.
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

