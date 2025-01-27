#### handleKeySet

```
protected Set<String> handleKeySet()
```
Returns a `Set` of the keys contained only
in this `ResourceBundle`.The default implementation returns a `Set` of the
keys returned by the `getKeys` method except
for the ones for which the `handleGetObject` method returns `null`. Once the
`Set` has been created, the value is kept in this
`ResourceBundle` in order to avoid producing the
same `Set` in subsequent calls. Subclasses can
override this method for faster handling.
Returns:
a `Set` of the keys contained only in this
`ResourceBundle`
Since:
1.6




