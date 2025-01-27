#### before

```
public boolean before(Object when)
```
Returns whether this `Calendar` represents a time
before the time represented by the specified
`Object`. This method is equivalent to:
```

         compareTo(when) < 0
 
```
if and only if `when` is a `Calendar`
instance. Otherwise, the method returns `false`.
Parameters:
`when` - the `Object` to be compared
Returns:
`true` if the time of this
`Calendar` is before the time represented by
`when`; `false` otherwise.
See Also:
`compareTo(Calendar)`

