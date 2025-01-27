#### hashCode

```
int hashCode()
```
Returns the hash code value for this map. The hash code of a map is
defined to be the sum of the hash codes of each entry in the map's
entrySet() view. This ensures that m1.equals(m2)
implies that m1.hashCode()==m2.hashCode() for any two maps
m1 and m2, as required by the general contract of
`Object.hashCode()`.
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this map
See Also:
`Map.Entry.hashCode()`,
`Object.equals(Object)`,
`equals(Object)`

