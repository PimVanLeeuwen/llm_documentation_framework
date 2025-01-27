#### hashCode

```
int hashCode()
```
Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a null element is defined to be zero.
This ensures that s1.equals(s2) implies that
s1.hashCode()==s2.hashCode() for any two sets s1
and s2, as required by the general contract of
`Object.hashCode()`.
Specified by:
`hashCode` in interface `Collection<E>`
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this set
See Also:
`Object.equals(Object)`,
`equals(Object)`

