#### nextElement

```
public Object nextElement()
```
Returns the same value as the `nextToken` method,
except that its declared return value is `Object` rather than
`String`. It exists so that this class can implement the
`Enumeration` interface.
Specified by:
`nextElement` in interface `Enumeration<Object>`
Returns:
the next token in the string.
Throws:
`NoSuchElementException` - if there are no more tokens in this
tokenizer's string.
See Also:
`Enumeration`,
`nextToken()`

