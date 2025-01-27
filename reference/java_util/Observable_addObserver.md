#### addObserver

```
public void addObserver(Observer o)
```
Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.
Parameters:
`o` - an observer to be added.
Throws:
`NullPointerException` - if the parameter o is null.

