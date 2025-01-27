#### getActualMinimum

```
public int getActualMinimum(int field)
```
Returns the minimum value that the specified calendar field
could have, given the time value of this `Calendar`.The default implementation of this method uses an iterative
algorithm to determine the actual minimum value for the
calendar field. Subclasses should, if possible, override this
with a more efficient implementation - in many cases, they can
simply return `getMinimum()`.
Parameters:
`field` - the calendar field
Returns:
the minimum of the given calendar field for the time
value of this `Calendar`
Since:
1.2
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMaximum(int)`

