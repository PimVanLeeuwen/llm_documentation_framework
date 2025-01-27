#### equals

```
public boolean equals(Object o)
```
Compares the specified Object with this Vector for equality. Returns
true if and only if the specified Object is also a List, both Lists
have the same size, and all corresponding pairs of elements in the two
Lists are equal. (Two elements `e1` and
`e2` are equal if `(e1==null ? e2==null :
e1.equals(e2))`.) In other words, two Lists are defined to be
equal if they contain the same elements in the same order.
Specified by:
`equals` in interface `Collection<E>`
Specified by:
`equals` in interface `List<E>`
Overrides:
`equals` in class `AbstractList<E>`
Parameters:
`o` - the Object to be compared for equality with this Vector
Returns:
true if the specified Object is equal to this Vector
See Also:
`Object.hashCode()`,
`HashMap`

