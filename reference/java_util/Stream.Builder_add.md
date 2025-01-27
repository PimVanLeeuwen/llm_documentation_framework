#### add

```
default Stream.Builder<T> add(T t)
```
Adds an element to the stream being built.
Implementation Requirements:
The default implementation behaves as if:
```

     accept(t)
     return this;
 
```

Parameters:
`t` - the element to add
Returns:
`this` builder
Throws:
`IllegalStateException` - if the builder has already transitioned to
the built state

