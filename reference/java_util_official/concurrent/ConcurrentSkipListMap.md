

ConcurrentSkipListMap (Java Platform SE 8 )
















































<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ConcurrentSkipListMap (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10,"i9":10,"i10":10,"i11":10,"i12":10,"i13":10,"i14":10,"i15":10,"i16":10,"i17":10,"i18":10,"i19":10,"i20":10,"i21":10,"i22":10,"i23":10,"i24":10,"i25":10,"i26":10,"i27":10,"i28":10,"i29":10,"i30":10,"i31":10,"i32":10,"i33":10,"i34":10,"i35":10,"i36":10,"i37":10,"i38":10,"i39":10,"i40":10,"i41":10,"i42":10,"i43":10,"i44":10,"i45":10,"i46":10,"i47":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact1, compact2, compact3
java.util.concurrentClass ConcurrentSkipListMap<K,V>
java.lang.Objectjava.util.AbstractMap<K,V>java.util.concurrent.ConcurrentSkipListMap<K,V>
Type Parameters:
`K` - the type of keys maintained by this map
`V` - the type of mapped values

All Implemented Interfaces:
Serializable, Cloneable, ConcurrentMap<K,V>, ConcurrentNavigableMap<K,V>, Map<K,V>, NavigableMap<K,V>, SortedMap<K,V>


```
public class ConcurrentSkipListMap<K,V>
extends AbstractMap<K,V>
implements ConcurrentNavigableMap<K,V>, Cloneable, Serializable
```
A scalable concurrent `ConcurrentNavigableMap` implementation.
The map is sorted according to the natural
ordering of its keys, or by a `Comparator` provided at map
creation time, depending on which constructor is used.This class implements a concurrent variant of SkipLists
providing expected average log(n) time cost for the
`containsKey`, `get`, `put` and
`remove` operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.Iterators and spliterators are
weakly consistent.Ascending key ordered views and their iterators are faster than
descending ones.All `Map.Entry` pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do not support the `Entry.setValue`
method. (Note however that it is possible to change mappings in the
associated map using `put`, `putIfAbsent`, or
`replace`, depending on exactly which effect you need.)Beware that, unlike in most collections, the `size`
method is not a constant-time operation. Because of the
asynchronous nature of these maps, determining the current number
of elements requires a traversal of the elements, and so may report
inaccurate results if this collection is modified during traversal.
Additionally, the bulk operations `putAll`, `equals`,
`toArray`, `containsValue`, and `clear` are
not guaranteed to be performed atomically. For example, an
iterator operating concurrently with a `putAll` operation
might view only some of the added elements.This class and its views and iterators implement all of the
optional methods of the `Map` and `Iterator`
interfaces. Like most other concurrent collections, this class does
not permit the use of `null` keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.This class is a member of the
Java Collections Framework.
Since:
1.6
See Also:
Serialized Form

### Nested Class Summary

### Nested classes/interfaces inherited from class java.util.AbstractMap

`AbstractMap.SimpleEntry<K,V>, AbstractMap.SimpleImmutableEntry<K,V>`

### Nested classes/interfaces inherited from interface java.util.Map

`Map.Entry<K,V>`

### Constructor Summary

Constructors Constructor and Description`ConcurrentSkipListMap()`
Constructs a new, empty map, sorted according to the
natural ordering of the keys.`ConcurrentSkipListMap(Comparator<? super K> comparator)`
Constructs a new, empty map, sorted according to the specified
comparator.`ConcurrentSkipListMap(Map<? extends K,? extends V> m)`
Constructs a new map containing the same mappings as the given map,
sorted according to the natural ordering of
the keys.`ConcurrentSkipListMap(SortedMap<K,? extends V> m)`
Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Map.Entry<K,V>``ceilingEntry(K key)`
Returns a key-value mapping associated with the least key
greater than or equal to the given key, or `null` if
there is no such entry.`K``ceilingKey(K key)`
Returns the least key greater than or equal to the given key,
or `null` if there is no such key.`void``clear()`
Removes all of the mappings from this map.`ConcurrentSkipListMap<K,V>``clone()`
Returns a shallow copy of this `ConcurrentSkipListMap`
instance.`Comparator<? super K>``comparator()`
Returns the comparator used to order the keys in this map, or
`null` if this map uses the natural ordering of its keys.`V``compute(K key,
BiFunction<? super K,? super V,? extends V> remappingFunction)`
Attempts to compute a mapping for the specified key and its
current mapped value (or `null` if there is no current
mapping).`V``computeIfAbsent(K key,
Function<? super K,? extends V> mappingFunction)`
If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless `null`.`V``computeIfPresent(K key,
BiFunction<? super K,? super V,? extends V> remappingFunction)`
If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value.`boolean``containsKey(Object key)`
Returns `true` if this map contains a mapping for the specified
key.`boolean``containsValue(Object value)`
Returns `true` if this map maps one or more keys to the
specified value.`NavigableSet<K>``descendingKeySet()`
Returns a reverse order `NavigableSet` view of the keys contained in this map.`ConcurrentNavigableMap<K,V>``descendingMap()`
Returns a reverse order view of the mappings contained in this map.`Set<Map.Entry<K,V>>``entrySet()`
Returns a `Set` view of the mappings contained in this map.`boolean``equals(Object o)`
Compares the specified object with this map for equality.`Map.Entry<K,V>``firstEntry()`
Returns a key-value mapping associated with the least
key in this map, or `null` if the map is empty.`K``firstKey()`
Returns the first (lowest) key currently in this map.`Map.Entry<K,V>``floorEntry(K key)`
Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or `null` if there
is no such key.`K``floorKey(K key)`
Returns the greatest key less than or equal to the given key,
or `null` if there is no such key.`void``forEach(BiConsumer<? super K,? super V> action)`
Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception.`V``get(Object key)`
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.`V``getOrDefault(Object key,
V defaultValue)`
Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.`ConcurrentNavigableMap<K,V>``headMap(K toKey)`
Returns a view of the portion of this map whose keys are
strictly less than `toKey`.`ConcurrentNavigableMap<K,V>``headMap(K toKey,
boolean inclusive)`
Returns a view of the portion of this map whose keys are less than (or
equal to, if `inclusive` is true) `toKey`.`Map.Entry<K,V>``higherEntry(K key)`
Returns a key-value mapping associated with the least key
strictly greater than the given key, or `null` if there
is no such key.`K``higherKey(K key)`
Returns the least key strictly greater than the given key, or
`null` if there is no such key.`boolean``isEmpty()`
Returns `true` if this map contains no key-value mappings.`NavigableSet<K>``keySet()`
Returns a `NavigableSet` view of the keys contained in this map.`Map.Entry<K,V>``lastEntry()`
Returns a key-value mapping associated with the greatest
key in this map, or `null` if the map is empty.`K``lastKey()`
Returns the last (highest) key currently in this map.`Map.Entry<K,V>``lowerEntry(K key)`
Returns a key-value mapping associated with the greatest key
strictly less than the given key, or `null` if there is
no such key.`K``lowerKey(K key)`
Returns the greatest key strictly less than the given key, or
`null` if there is no such key.`V``merge(K key,
V value,
BiFunction<? super V,? super V,? extends V> remappingFunction)`
If the specified key is not already associated with a value,
associates it with the given value.`NavigableSet<K>``navigableKeySet()`
Returns a `NavigableSet` view of the keys contained in this map.`Map.Entry<K,V>``pollFirstEntry()`
Removes and returns a key-value mapping associated with
the least key in this map, or `null` if the map is empty.`Map.Entry<K,V>``pollLastEntry()`
Removes and returns a key-value mapping associated with
the greatest key in this map, or `null` if the map is empty.`V``put(K key,
V value)`
Associates the specified value with the specified key in this map.`V``putIfAbsent(K key,
V value)`
If the specified key is not already associated
with a value, associate it with the given value.`V``remove(Object key)`
Removes the mapping for the specified key from this map if present.`boolean``remove(Object key,
Object value)`
Removes the entry for a key only if currently mapped to a given value.`V``replace(K key,
V value)`
Replaces the entry for a key only if currently mapped to some value.`boolean``replace(K key,
V oldValue,
V newValue)`
Replaces the entry for a key only if currently mapped to a given value.`void``replaceAll(BiFunction<? super K,? super V,? extends V> function)`
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed or the
function throws an exception.`int``size()`
Returns the number of key-value mappings in this map.`ConcurrentNavigableMap<K,V>``subMap(K fromKey,
boolean fromInclusive,
K toKey,
boolean toInclusive)`
Returns a view of the portion of this map whose keys range from
`fromKey` to `toKey`.`ConcurrentNavigableMap<K,V>``subMap(K fromKey,
K toKey)`
Returns a view of the portion of this map whose keys range from
`fromKey`, inclusive, to `toKey`, exclusive.`ConcurrentNavigableMap<K,V>``tailMap(K fromKey)`
Returns a view of the portion of this map whose keys are
greater than or equal to `fromKey`.`ConcurrentNavigableMap<K,V>``tailMap(K fromKey,
boolean inclusive)`
Returns a view of the portion of this map whose keys are greater than (or
equal to, if `inclusive` is true) `fromKey`.`Collection<V>``values()`
Returns a `Collection` view of the values contained in this map.

### Methods inherited from class java.util.AbstractMap

`hashCode, putAll, toString`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.Map

`hashCode, putAll`

### Constructor Detail

#### ConcurrentSkipListMap

```
public ConcurrentSkipListMap()
```
Constructs a new, empty map, sorted according to the
natural ordering of the keys.

#### ConcurrentSkipListMap

```
public ConcurrentSkipListMap(Comparator<? super K> comparator)
```
Constructs a new, empty map, sorted according to the specified
comparator.
Parameters:
`comparator` - the comparator that will be used to order this map.
If `null`, the natural
ordering of the keys will be used.

#### ConcurrentSkipListMap

```
public ConcurrentSkipListMap(Map<? extends K,? extends V> m)
```
Constructs a new map containing the same mappings as the given map,
sorted according to the natural ordering of
the keys.
Parameters:
`m` - the map whose mappings are to be placed in this map
Throws:
`ClassCastException` - if the keys in `m` are not
`Comparable`, or are not mutually comparable
`NullPointerException` - if the specified map or any of its keys
or values are null

#### ConcurrentSkipListMap

```
public ConcurrentSkipListMap(SortedMap<K,? extends V> m)
```
Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.
Parameters:
`m` - the sorted map whose mappings are to be placed in this
map, and whose comparator is to be used to sort this map
Throws:
`NullPointerException` - if the specified sorted map or any of
its keys or values are null

### Method Detail

#### clone

```
public ConcurrentSkipListMap<K,V> clone()
```
Returns a shallow copy of this `ConcurrentSkipListMap`
instance. (The keys and values themselves are not cloned.)
Overrides:
`clone` in class `AbstractMap<K,V>`
Returns:
a shallow copy of this map
See Also:
`Cloneable`

#### containsKey

```
public boolean containsKey(Object key)
```
Returns `true` if this map contains a mapping for the specified
key.
Specified by:
`containsKey` in interface `Map<K,V>`
Overrides:
`containsKey` in class `AbstractMap<K,V>`
Parameters:
`key` - key whose presence in this map is to be tested
Returns:
`true` if this map contains a mapping for the specified key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### get

```
public V get(Object key)
```
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.More formally, if this map contains a mapping from a key
`k` to a value `v` such that `key` compares
equal to `k` according to the map's ordering, then this
method returns `v`; otherwise it returns `null`.
(There can be at most one such mapping.)
Specified by:
`get` in interface `Map<K,V>`
Overrides:
`get` in class `AbstractMap<K,V>`
Parameters:
`key` - the key whose associated value is to be returned
Returns:
the value to which the specified key is mapped, or
`null` if this map contains no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### getOrDefault

```
public V getOrDefault(Object key,
                      V defaultValue)
```
Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.
Specified by:
`getOrDefault` in interface `ConcurrentMap<K,V>`
Specified by:
`getOrDefault` in interface `Map<K,V>`
Parameters:
`key` - the key
`defaultValue` - the value to return if this map contains
no mapping for the given key
Returns:
the mapping for the key, if present; else the defaultValue
Throws:
`NullPointerException` - if the specified key is null
Since:
1.8

#### put

```
public V put(K key,
             V value)
```
Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.
Specified by:
`put` in interface `Map<K,V>`
Overrides:
`put` in class `AbstractMap<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

#### remove

```
public V remove(Object key)
```
Removes the mapping for the specified key from this map if present.
Specified by:
`remove` in interface `Map<K,V>`
Overrides:
`remove` in class `AbstractMap<K,V>`
Parameters:
`key` - key for which mapping should be removed
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### containsValue

```
public boolean containsValue(Object value)
```
Returns `true` if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.
Specified by:
`containsValue` in interface `Map<K,V>`
Overrides:
`containsValue` in class `AbstractMap<K,V>`
Parameters:
`value` - value whose presence in this map is to be tested
Returns:
`true` if a mapping to `value` exists;
`false` otherwise
Throws:
`NullPointerException` - if the specified value is null

#### size

```
public int size()
```
Returns the number of key-value mappings in this map. If this map
contains more than `Integer.MAX_VALUE` elements, it
returns `Integer.MAX_VALUE`.Beware that, unlike in most collections, this method is
NOT a constant-time operation. Because of the
asynchronous nature of these maps, determining the current
number of elements requires traversing them all to count them.
Additionally, it is possible for the size to change during
execution of this method, in which case the returned result
will be inaccurate. Thus, this method is typically not very
useful in concurrent applications.
Specified by:
`size` in interface `Map<K,V>`
Overrides:
`size` in class `AbstractMap<K,V>`
Returns:
the number of elements in this map

#### isEmpty

```
public boolean isEmpty()
```
Returns `true` if this map contains no key-value mappings.
Specified by:
`isEmpty` in interface `Map<K,V>`
Overrides:
`isEmpty` in class `AbstractMap<K,V>`
Returns:
`true` if this map contains no key-value mappings

#### clear

```
public void clear()
```
Removes all of the mappings from this map.
Specified by:
`clear` in interface `Map<K,V>`
Overrides:
`clear` in class `AbstractMap<K,V>`

#### computeIfAbsent

```
public V computeIfAbsent(K key,
                         Function<? super K,? extends V> mappingFunction)
```
If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless `null`. The function
is NOT guaranteed to be applied once atomically only
if the value is not present.
Specified by:
`computeIfAbsent` in interface `ConcurrentMap<K,V>`
Specified by:
`computeIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null
Throws:
`NullPointerException` - if the specified key is null
or the mappingFunction is null
Since:
1.8

#### computeIfPresent

```
public V computeIfPresent(K key,
                          BiFunction<? super K,? super V,? extends V> remappingFunction)
```
If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is NOT guaranteed to be applied
once atomically.
Specified by:
`computeIfPresent` in interface `ConcurrentMap<K,V>`
Specified by:
`computeIfPresent` in interface `Map<K,V>`
Parameters:
`key` - key with which a value may be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key is null
or the remappingFunction is null
Since:
1.8

#### compute

```
public V compute(K key,
                 BiFunction<? super K,? super V,? extends V> remappingFunction)
```
Attempts to compute a mapping for the specified key and its
current mapped value (or `null` if there is no current
mapping). The function is NOT guaranteed to be applied
once atomically.
Specified by:
`compute` in interface `ConcurrentMap<K,V>`
Specified by:
`compute` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key is null
or the remappingFunction is null
Since:
1.8

#### merge

```
public V merge(K key,
               V value,
               BiFunction<? super V,? super V,? extends V> remappingFunction)
```
If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if `null`. The function is NOT
guaranteed to be applied once atomically.
Specified by:
`merge` in interface `ConcurrentMap<K,V>`
Specified by:
`merge` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - the value to use if absent
`remappingFunction` - the function to recompute a value if present
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key or value is null
or the remappingFunction is null
Since:
1.8

#### keySet

```
public NavigableSet<K> keySet()
```
Returns a `NavigableSet` view of the keys contained in this map.The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports `Spliterator.CONCURRENT`,
`Spliterator.NONNULL`, `Spliterator.SORTED` and
`Spliterator.ORDERED`, with an encounter order that is ascending
key order. The spliterator's comparator (see
`Spliterator.getComparator()`) is `null` if
the map's comparator (see `comparator()`) is `null`.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.The view's iterators and spliterators are
weakly consistent.This method is equivalent to method `navigableKeySet`.
Specified by:
`keySet` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`keySet` in interface `Map<K,V>`
Specified by:
`keySet` in interface `SortedMap<K,V>`
Overrides:
`keySet` in class `AbstractMap<K,V>`
Returns:
a navigable set view of the keys in this map

#### navigableKeySet

```
public NavigableSet<K> navigableKeySet()
```
Description copied from interface: `ConcurrentNavigableMap`
Returns a `NavigableSet` view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.The view's iterators and spliterators are
weakly consistent.
Specified by:
`navigableKeySet` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`navigableKeySet` in interface `NavigableMap<K,V>`
Returns:
a navigable set view of the keys in this map

#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports `Spliterator.CONCURRENT`, `Spliterator.NONNULL` and
`Spliterator.ORDERED`, with an encounter order that is ascending
order of the corresponding keys.The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the `Iterator.remove`,
`Collection.remove`, `removeAll`,
`retainAll` and `clear` operations. It does not
support the `add` or `addAll` operations.The view's iterators and spliterators are
weakly consistent.
Specified by:
`values` in interface `Map<K,V>`
Specified by:
`values` in interface `SortedMap<K,V>`
Overrides:
`values` in class `AbstractMap<K,V>`
Returns:
a collection view of the values contained in this map

#### entrySet

```
public Set<Map.Entry<K,V>> entrySet()
```
Returns a `Set` view of the mappings contained in this map.The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports `Spliterator.CONCURRENT`,
`Spliterator.NONNULL`, `Spliterator.SORTED` and
`Spliterator.ORDERED`, with an encounter order that is ascending
key order.The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll` and `clear`
operations. It does not support the `add` or
`addAll` operations.The view's iterators and spliterators are
weakly consistent.The `Map.Entry` elements traversed by the `iterator`
or `spliterator` do not support the `setValue`
operation.
Specified by:
`entrySet` in interface `Map<K,V>`
Specified by:
`entrySet` in interface `SortedMap<K,V>`
Specified by:
`entrySet` in class `AbstractMap<K,V>`
Returns:
a set view of the mappings contained in this map,
sorted in ascending key order

#### descendingMap

```
public ConcurrentNavigableMap<K,V> descendingMap()
```
Description copied from interface: `ConcurrentNavigableMap`
Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa.The returned map has an ordering equivalent to
`Collections.reverseOrder``(comparator())`.
The expression `m.descendingMap().descendingMap()` returns a
view of `m` essentially equivalent to `m`.
Specified by:
`descendingMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`descendingMap` in interface `NavigableMap<K,V>`
Returns:
a reverse order view of this map

#### descendingKeySet

```
public NavigableSet<K> descendingKeySet()
```
Description copied from interface: `ConcurrentNavigableMap`
Returns a reverse order `NavigableSet` view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.The view's iterators and spliterators are
weakly consistent.
Specified by:
`descendingKeySet` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`descendingKeySet` in interface `NavigableMap<K,V>`
Returns:
a reverse order navigable set view of the keys in this map

#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this map for equality.
Returns `true` if the given object is also a map and the
two maps represent the same mappings. More formally, two maps
`m1` and `m2` represent the same mappings if
`m1.entrySet().equals(m2.entrySet())`. This
operation may return misleading results if either map is
concurrently modified during execution of this method.
Specified by:
`equals` in interface `Map<K,V>`
Overrides:
`equals` in class `AbstractMap<K,V>`
Parameters:
`o` - object to be compared for equality with this map
Returns:
`true` if the specified object is equal to this map
See Also:
`Object.hashCode()`,
`HashMap`

#### putIfAbsent

```
public V putIfAbsent(K key,
                     V value)
```
If the specified key is not already associated
with a value, associate it with the given value.
This is equivalent to
```
 
 if (!map.containsKey(key))
   return map.put(key, value);
 else
   return map.get(key);
 
```
except that the action is performed atomically.
Specified by:
`putIfAbsent` in interface `ConcurrentMap<K,V>`
Specified by:
`putIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key,
or `null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

#### remove

```
public boolean remove(Object key,
                      Object value)
```
Removes the entry for a key only if currently mapped to a given value.
This is equivalent to
```
 
 if (map.containsKey(key) && Objects.equals(map.get(key), value)) {
   map.remove(key);
   return true;
 } else
   return false;
 
```
except that the action is performed atomically.
Specified by:
`remove` in interface `ConcurrentMap<K,V>`
Specified by:
`remove` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`value` - value expected to be associated with the specified key
Returns:
`true` if the value was removed
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### replace

```
public boolean replace(K key,
                       V oldValue,
                       V newValue)
```
Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to
```
 
 if (map.containsKey(key) && Objects.equals(map.get(key), oldValue)) {
   map.put(key, newValue);
   return true;
 } else
   return false;
 
```
except that the action is performed atomically.
Specified by:
`replace` in interface `ConcurrentMap<K,V>`
Specified by:
`replace` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`oldValue` - value expected to be associated with the specified key
`newValue` - value to be associated with the specified key
Returns:
`true` if the value was replaced
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if any of the arguments are null

#### replace

```
public V replace(K key,
                 V value)
```
Replaces the entry for a key only if currently mapped to some value.
This is equivalent to
```
 
 if (map.containsKey(key)) {
   return map.put(key, value);
 } else
   return null;
 
```
except that the action is performed atomically.
Specified by:
`replace` in interface `ConcurrentMap<K,V>`
Specified by:
`replace` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key,
or `null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

#### comparator

```
public Comparator<? super K> comparator()
```
Description copied from interface: `SortedMap`
Returns the comparator used to order the keys in this map, or
`null` if this map uses the natural ordering of its keys.
Specified by:
`comparator` in interface `SortedMap<K,V>`
Returns:
the comparator used to order the keys in this map,
or `null` if this map uses the natural ordering
of its keys

#### firstKey

```
public K firstKey()
```
Description copied from interface: `SortedMap`
Returns the first (lowest) key currently in this map.
Specified by:
`firstKey` in interface `SortedMap<K,V>`
Returns:
the first (lowest) key currently in this map
Throws:
`NoSuchElementException` - if this map is empty

#### lastKey

```
public K lastKey()
```
Description copied from interface: `SortedMap`
Returns the last (highest) key currently in this map.
Specified by:
`lastKey` in interface `SortedMap<K,V>`
Returns:
the last (highest) key currently in this map
Throws:
`NoSuchElementException` - if this map is empty

#### subMap

```
public ConcurrentNavigableMap<K,V> subMap(K fromKey,
                                          boolean fromInclusive,
                                          K toKey,
                                          boolean toInclusive)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys range from
`fromKey` to `toKey`. If `fromKey` and
`toKey` are equal, the returned map is empty unless
`fromInclusive` and `toInclusive` are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.
Specified by:
`subMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`subMap` in interface `NavigableMap<K,V>`
Parameters:
`fromKey` - low endpoint of the keys in the returned map
`fromInclusive` - `true` if the low endpoint
is to be included in the returned view
`toKey` - high endpoint of the keys in the returned map
`toInclusive` - `true` if the high endpoint
is to be included in the returned view
Returns:
a view of the portion of this map whose keys range from
`fromKey` to `toKey`
Throws:
`ClassCastException` - if `fromKey` and `toKey`
cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if `fromKey` or `toKey`
cannot be compared to keys currently in the map.
`NullPointerException` - if `fromKey` or `toKey` is null
`IllegalArgumentException` - if `fromKey` is greater than
`toKey`; or if this map itself has a restricted
range, and `fromKey` or `toKey` lies
outside the bounds of the range

#### headMap

```
public ConcurrentNavigableMap<K,V> headMap(K toKey,
                                           boolean inclusive)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys are less than (or
equal to, if `inclusive` is true) `toKey`. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.
Specified by:
`headMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`headMap` in interface `NavigableMap<K,V>`
Parameters:
`toKey` - high endpoint of the keys in the returned map
`inclusive` - `true` if the high endpoint
is to be included in the returned view
Returns:
a view of the portion of this map whose keys are less than
(or equal to, if `inclusive` is true) `toKey`
Throws:
`ClassCastException` - if `toKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `toKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `toKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `toKey` is null
`IllegalArgumentException` - if this map itself has a
restricted range, and `toKey` lies outside the
bounds of the range

#### tailMap

```
public ConcurrentNavigableMap<K,V> tailMap(K fromKey,
                                           boolean inclusive)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys are greater than (or
equal to, if `inclusive` is true) `fromKey`. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.
Specified by:
`tailMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`tailMap` in interface `NavigableMap<K,V>`
Parameters:
`fromKey` - low endpoint of the keys in the returned map
`inclusive` - `true` if the low endpoint
is to be included in the returned view
Returns:
a view of the portion of this map whose keys are greater than
(or equal to, if `inclusive` is true) `fromKey`
Throws:
`ClassCastException` - if `fromKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `fromKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `fromKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `fromKey` is null
`IllegalArgumentException` - if this map itself has a
restricted range, and `fromKey` lies outside the
bounds of the range

#### subMap

```
public ConcurrentNavigableMap<K,V> subMap(K fromKey,
                                          K toKey)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys range from
`fromKey`, inclusive, to `toKey`, exclusive. (If
`fromKey` and `toKey` are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.Equivalent to `subMap(fromKey, true, toKey, false)`.
Specified by:
`subMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`subMap` in interface `NavigableMap<K,V>`
Specified by:
`subMap` in interface `SortedMap<K,V>`
Parameters:
`fromKey` - low endpoint (inclusive) of the keys in the returned map
`toKey` - high endpoint (exclusive) of the keys in the returned map
Returns:
a view of the portion of this map whose keys range from
`fromKey`, inclusive, to `toKey`, exclusive
Throws:
`ClassCastException` - if `fromKey` and `toKey`
cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if `fromKey` or `toKey`
cannot be compared to keys currently in the map.
`NullPointerException` - if `fromKey` or `toKey` is null
`IllegalArgumentException` - if `fromKey` is greater than
`toKey`; or if this map itself has a restricted
range, and `fromKey` or `toKey` lies
outside the bounds of the range

#### headMap

```
public ConcurrentNavigableMap<K,V> headMap(K toKey)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys are
strictly less than `toKey`. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.Equivalent to `headMap(toKey, false)`.
Specified by:
`headMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`headMap` in interface `NavigableMap<K,V>`
Specified by:
`headMap` in interface `SortedMap<K,V>`
Parameters:
`toKey` - high endpoint (exclusive) of the keys in the returned map
Returns:
a view of the portion of this map whose keys are strictly
less than `toKey`
Throws:
`ClassCastException` - if `toKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `toKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `toKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `toKey` is null
`IllegalArgumentException` - if this map itself has a
restricted range, and `toKey` lies outside the
bounds of the range

#### tailMap

```
public ConcurrentNavigableMap<K,V> tailMap(K fromKey)
```
Description copied from interface: `NavigableMap`
Returns a view of the portion of this map whose keys are
greater than or equal to `fromKey`. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.Equivalent to `tailMap(fromKey, true)`.
Specified by:
`tailMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`tailMap` in interface `NavigableMap<K,V>`
Specified by:
`tailMap` in interface `SortedMap<K,V>`
Parameters:
`fromKey` - low endpoint (inclusive) of the keys in the returned map
Returns:
a view of the portion of this map whose keys are greater
than or equal to `fromKey`
Throws:
`ClassCastException` - if `fromKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `fromKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `fromKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `fromKey` is null
`IllegalArgumentException` - if this map itself has a
restricted range, and `fromKey` lies outside the
bounds of the range

#### lowerEntry

```
public Map.Entry<K,V> lowerEntry(K key)
```
Returns a key-value mapping associated with the greatest key
strictly less than the given key, or `null` if there is
no such key. The returned entry does not support the
`Entry.setValue` method.
Specified by:
`lowerEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the greatest key less than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### lowerKey

```
public K lowerKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the greatest key strictly less than the given key, or
`null` if there is no such key.
Specified by:
`lowerKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the greatest key less than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### floorEntry

```
public Map.Entry<K,V> floorEntry(K key)
```
Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or `null` if there
is no such key. The returned entry does not support
the `Entry.setValue` method.
Specified by:
`floorEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the greatest key less than or equal to
`key`, or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### floorKey

```
public K floorKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the greatest key less than or equal to the given key,
or `null` if there is no such key.
Specified by:
`floorKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the greatest key less than or equal to `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### ceilingEntry

```
public Map.Entry<K,V> ceilingEntry(K key)
```
Returns a key-value mapping associated with the least key
greater than or equal to the given key, or `null` if
there is no such entry. The returned entry does not
support the `Entry.setValue` method.
Specified by:
`ceilingEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the least key greater than or equal to
`key`, or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### ceilingKey

```
public K ceilingKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the least key greater than or equal to the given key,
or `null` if there is no such key.
Specified by:
`ceilingKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the least key greater than or equal to `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### higherEntry

```
public Map.Entry<K,V> higherEntry(K key)
```
Returns a key-value mapping associated with the least key
strictly greater than the given key, or `null` if there
is no such key. The returned entry does not support
the `Entry.setValue` method.
Specified by:
`higherEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the least key greater than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### higherKey

```
public K higherKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the least key strictly greater than the given key, or
`null` if there is no such key.
Specified by:
`higherKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the least key greater than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

#### firstEntry

```
public Map.Entry<K,V> firstEntry()
```
Returns a key-value mapping associated with the least
key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`firstEntry` in interface `NavigableMap<K,V>`
Returns:
an entry with the least key,
or `null` if this map is empty

#### lastEntry

```
public Map.Entry<K,V> lastEntry()
```
Returns a key-value mapping associated with the greatest
key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`lastEntry` in interface `NavigableMap<K,V>`
Returns:
an entry with the greatest key,
or `null` if this map is empty

#### pollFirstEntry

```
public Map.Entry<K,V> pollFirstEntry()
```
Removes and returns a key-value mapping associated with
the least key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`pollFirstEntry` in interface `NavigableMap<K,V>`
Returns:
the removed first entry of this map,
or `null` if this map is empty

#### pollLastEntry

```
public Map.Entry<K,V> pollLastEntry()
```
Removes and returns a key-value mapping associated with
the greatest key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`pollLastEntry` in interface `NavigableMap<K,V>`
Returns:
the removed last entry of this map,
or `null` if this map is empty

#### forEach

```
public void forEach(BiConsumer<? super K,? super V> action)
```
Description copied from interface: `ConcurrentMap`
Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.
Specified by:
`forEach` in interface `ConcurrentMap<K,V>`
Specified by:
`forEach` in interface `Map<K,V>`
Parameters:
`action` - The action to be performed for each entry

#### replaceAll

```
public void replaceAll(BiFunction<? super K,? super V,? extends V> function)
```
Description copied from interface: `ConcurrentMap`
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed or the
function throws an exception. Exceptions thrown by the function are
relayed to the caller.
Specified by:
`replaceAll` in interface `ConcurrentMap<K,V>`
Specified by:
`replaceAll` in interface `Map<K,V>`
Parameters:
`function` - the function to apply to each entry




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

