#### clearChanged

```
protected void clearChanged()
```
Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the hasChanged method will now return false.
This method is called automatically by the
`notifyObservers` methods.
See Also:
`notifyObservers()`,
`notifyObservers(java.lang.Object)`

