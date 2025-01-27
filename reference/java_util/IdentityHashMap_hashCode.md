#### hashCode

```
public int hashCode()
```
Returns the hash code value for this map. The hash code of a map is
defined to be the sum of the hash codes of each entry in the map's
entrySet() view. This ensures that m1.equals(m2)
implies that m1.hashCode()==m2.hashCode() for any two
IdentityHashMap instances m1 and m2, as
required by the general contract of `Object.hashCode()`.Owing to the reference-equality-based semantics of the
Map.Entry instances in the set returned by this map's
entrySet method, it is possible that the contractual
requirement of Object.hashCode mentioned in the previous
paragraph will be violated if one of the two objects being compared is
an IdentityHashMap instance and the other is a normal map.
Specified by:
`hashCode` in interface `Map<K,V>`
Overrides:
`hashCode` in class `AbstractMap<K,V>`
Returns:
the hash code value for this map
See Also:
`Object.equals(Object)`,
`equals(Object)`

