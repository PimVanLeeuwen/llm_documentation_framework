#### equals

```
public boolean equals(Object obj)
```
Indicates whether some other object is "equal to" this Optional. The
other object is considered equal if:it is also an `Optional` and;both instances have no value present or;the present values are "equal to" each other via `equals()`.
Overrides:
`equals` in class `Object`
Parameters:
`obj` - an object to be tested for equality
Returns:
{code true} if the other object is "equal to" this object
otherwise `false`
See Also:
`Object.hashCode()`,
`HashMap`

