#### hashCode

```
int hashCode()
```
Returns the hash code value for this map entry. The hash code
of a map entry e is defined to be:
```

     (e.getKey()==null   ? 0 : e.getKey().hashCode()) ^
     (e.getValue()==null ? 0 : e.getValue().hashCode())
 
```
This ensures that e1.equals(e2) implies that
e1.hashCode()==e2.hashCode() for any two Entries
e1 and e2, as required by the general
contract of Object.hashCode.
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this map entry
See Also:
`Object.hashCode()`,
`Object.equals(Object)`,
`equals(Object)`

