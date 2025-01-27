#### forEachRemaining

```
default void forEachRemaining(Consumer<? super E> action)
```
Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.
Implementation Requirements:
The default implementation behaves as if:
```

     while (hasNext())
         action.accept(next());
 
```

Parameters:
`action` - The action to be performed for each element
Throws:
`NullPointerException` - if the specified action is null
Since:
1.8




