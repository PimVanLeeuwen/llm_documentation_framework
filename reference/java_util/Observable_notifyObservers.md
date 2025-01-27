#### notifyObservers

```
public void notifyObservers(Object arg)
```
If this object has changed, as indicated by the
`hasChanged` method, then notify all of its observers
and then call the `clearChanged` method to indicate
that this object has no longer changed.Each observer has its `update` method called with two
arguments: this observable object and the `arg` argument.
Parameters:
`arg` - any object.
See Also:
`clearChanged()`,
`hasChanged()`,
`Observer.update(java.util.Observable, java.lang.Object)`

