#### ifPresent

```
public void ifPresent(Consumer<? super T> consumer)
```
If a value is present, invoke the specified consumer with the value,
otherwise do nothing.
Parameters:
`consumer` - block to be executed if a value is present
Throws:
`NullPointerException` - if value is present and `consumer` is
null

