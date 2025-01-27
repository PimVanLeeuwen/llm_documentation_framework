#### getActualMaximum

```
public int getActualMaximum(int field)
```
Returns the maximum value that the specified calendar field
could have, given the time value of this
`Calendar`. For example, the actual maximum value of
the `MONTH` field is 12 in some years, and 13 in
other years in the Hebrew calendar system.The default implementation of this method uses an iterative
algorithm to determine the actual maximum value for the
calendar field. Subclasses should, if possible, override this
with a more efficient implementation.
Parameters:
`field` - the calendar field
Returns:
the maximum of the given calendar field for the time
value of this `Calendar`
Since:
1.2
See Also:
`getMinimum(int)`,
`getMaximum(int)`,
`getGreatestMinimum(int)`,
`getLeastMaximum(int)`,
`getActualMinimum(int)`

