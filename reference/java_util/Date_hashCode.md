#### hashCode

```
public int hashCode()
```
Returns a hash code value for this object. The result is the
exclusive OR of the two halves of the primitive long
value returned by the `getTime()`
method. That is, the hash code is the value of the expression:
```

 (int)(this.getTime()^(this.getTime() >>> 32))
 
```

Overrides:
`hashCode` in class `Object`
Returns:
a hash code value for this object.
See Also:
`Object.equals(java.lang.Object)`,
`System.identityHashCode(java.lang.Object)`

