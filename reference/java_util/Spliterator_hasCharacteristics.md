#### hasCharacteristics

```
default boolean hasCharacteristics(int characteristics)
```
Returns `true` if this Spliterator's `characteristics()` contain all of the given characteristics.
Implementation Requirements:
The default implementation returns true if the corresponding bits
of the given characteristics are set.
Parameters:
`characteristics` - the characteristics to check for
Returns:
`true` if all the specified characteristics are present,
else `false`

