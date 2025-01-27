#### clone

```
public Object clone()
```
Returns a copy of the Attributes, implemented as follows:
```

     public Object clone() { return new Attributes(this); }
 
```
Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.
Overrides:
`clone` in class `Object`
Returns:
a clone of this instance.
See Also:
`Cloneable`




