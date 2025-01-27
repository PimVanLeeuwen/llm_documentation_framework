#### equals

```
public boolean equals(Object obj)
```
Compares this `Calendar` to the specified
`Object`. The result is `true` if and only if
the argument is a `Calendar` object of the same calendar
system that represents the same time value (millisecond offset from the
Epoch) under the same
`Calendar` parameters as this object.The `Calendar` parameters are the values represented
by the `isLenient`, `getFirstDayOfWeek`,
`getMinimalDaysInFirstWeek` and `getTimeZone`
methods. If there is any difference in those parameters
between the two `Calendar`s, this method returns
`false`.Use the `compareTo` method to
compare only the time values.
Overrides:
`equals` in class `Object`
Parameters:
`obj` - the object to compare with.
Returns:
`true` if this object is equal to `obj`;
`false` otherwise.
See Also:
`Object.hashCode()`,
`HashMap`

