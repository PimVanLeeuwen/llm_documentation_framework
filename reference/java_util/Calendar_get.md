#### get

```
public int get(int field)
```
Returns the value of the given calendar field. In lenient mode,
all calendar fields are normalized. In non-lenient mode, all
calendar fields are validated and this method throws an
exception if any calendar fields have out-of-range values. The
normalization and validation are handled by the
`complete()` method, which process is calendar
system dependent.
Parameters:
`field` - the given calendar field.
Returns:
the value for the given calendar field.
Throws:
`ArrayIndexOutOfBoundsException` - if the specified field is out of range
(`field < 0 || field >= FIELD_COUNT`).
See Also:
`set(int,int)`,
`complete()`

