#### ifPresent

```
public void ifPresent(DoubleConsumer consumer)
```
Have the specified consumer accept the value if a value is present,
otherwise do nothing.
Parameters:
`consumer` - block to be executed if a value is present
Throws:
`NullPointerException` - if value is present and `consumer` is
null

