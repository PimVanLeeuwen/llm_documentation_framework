#### comparingByKey

```
static <K,V> Comparator<Map.Entry<K,V>> comparingByKey(Comparator<? super K> cmp)
```
Returns a comparator that compares `Map.Entry` by key using the given
`Comparator`.The returned comparator is serializable if the specified comparator
is also serializable.
Type Parameters:
`K` - the type of the map keys
`V` - the type of the map values
Parameters:
`cmp` - the key `Comparator`
Returns:
a comparator that compares `Map.Entry` by the key.
Since:
1.8

