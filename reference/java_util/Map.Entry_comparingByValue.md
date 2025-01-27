#### comparingByValue

```
static <K,V> Comparator<Map.Entry<K,V>> comparingByValue(Comparator<? super V> cmp)
```
Returns a comparator that compares `Map.Entry` by value using the given
`Comparator`.The returned comparator is serializable if the specified comparator
is also serializable.
Type Parameters:
`K` - the type of the map keys
`V` - the type of the map values
Parameters:
`cmp` - the value `Comparator`
Returns:
a comparator that compares `Map.Entry` by the value.
Since:
1.8




