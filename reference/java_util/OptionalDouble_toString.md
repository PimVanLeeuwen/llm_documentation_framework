#### toString

```
public String toString()
```
Returns a string representation of the object. In general, the
`toString` method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.The `toString` method for class `Object`
returns a string consisting of the name of the class of which the
object is an instance, the at-sign character ``@`', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:
```

 getClass().getName() + '@' + Integer.toHexString(hashCode())
 
```
Returns a non-empty string representation of this object suitable for
debugging. The exact presentation format is unspecified and may vary
between implementations and versions.
Overrides:
`toString` in class `Object`
Implementation Requirements:
If a value is present the result must include its string
representation in the result. Empty and present instances must be
unambiguously differentiable.
Returns:
the string representation of this instance




