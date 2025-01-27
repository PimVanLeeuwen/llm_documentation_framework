#### hashCode

```
int hashCode()
```
Returns the hash code value for this collection. While the
Collection interface adds no stipulations to the general
contract for the Object.hashCode method, programmers should
take note that any class that overrides the Object.equals
method must also override the Object.hashCode method in order
to satisfy the general contract for the Object.hashCode method.
In particular, c1.equals(c2) implies that
c1.hashCode()==c2.hashCode().
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this collection
See Also:
`Object.hashCode()`,
`Object.equals(Object)`

