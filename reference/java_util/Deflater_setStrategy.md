#### setStrategy

```
public void setStrategy(int strategy)
```
Sets the compression strategy to the specified value.If the compression strategy is changed, the next invocation
of `deflate` will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.
Parameters:
`strategy` - the new compression strategy
Throws:
`IllegalArgumentException` - if the compression strategy is
invalid

