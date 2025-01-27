#### putValue

```
public String putValue(String name,
                       String value)
```
Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.This method is defined as:
```

      return (String)put(new Attributes.Name(name), value);
 
```

Parameters:
`name` - the attribute name as a string
`value` - the attribute value
Returns:
the previous value of the attribute, or null if none
Throws:
`IllegalArgumentException` - if the attribute name is invalid

