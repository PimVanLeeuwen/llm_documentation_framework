#### equals

```
public boolean equals(Object obj)
```
Compares two dates for equality.
The result is `true` if and only if the argument is
not `null` and is a `Date` object that
represents the same point in time, to the millisecond, as this object.Thus, two `Date` objects are equal if and only if the
`getTime` method returns the same `long`
value for both.
Overrides:
`equals` in class `Object`
Parameters:
`obj` - the object to compare with.
Returns:
`true` if the objects are the same;
`false` otherwise.
See Also:
`getTime()`

