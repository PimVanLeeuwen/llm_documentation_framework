

AbstractMap.SimpleImmutableEntry (Java Platform SE 8 )











<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="AbstractMap.SimpleImmutableEntry (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10};
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
java.utilClass AbstractMap.SimpleImmutableEntry<K,V>
java.lang.Objectjava.util.AbstractMap.SimpleImmutableEntry<K,V>
All Implemented Interfaces:
Serializable, Map.Entry<K,V>

Enclosing class:
AbstractMap<K,V>


```
public static class AbstractMap.SimpleImmutableEntry<K,V>
extends Object
implements Map.Entry<K,V>, Serializable
```
An Entry maintaining an immutable key and value. This class
does not support method setValue. This class may be
convenient in methods that return thread-safe snapshots of
key-value mappings.
Since:
1.6
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`SimpleImmutableEntry(K key,
V value)`
Creates an entry representing a mapping from the specified
key to the specified value.`SimpleImmutableEntry(Map.Entry<? extends K,? extends V> entry)`
Creates an entry representing the same mapping as the
specified entry.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`boolean``equals(Object o)`
Compares the specified object with this entry for equality.`K``getKey()`
Returns the key corresponding to this entry.`V``getValue()`
Returns the value corresponding to this entry.`int``hashCode()`
Returns the hash code value for this map entry.`V``setValue(V value)`
Replaces the value corresponding to this entry with the specified
value (optional operation).`String``toString()`
Returns a String representation of this map entry.

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.Map.Entry

`comparingByKey, comparingByKey, comparingByValue, comparingByValue`

### Constructor Detail

#### SimpleImmutableEntry

```
public SimpleImmutableEntry(K key,
                            V value)
```
Creates an entry representing a mapping from the specified
key to the specified value.
Parameters:
`key` - the key represented by this entry
`value` - the value represented by this entry

#### SimpleImmutableEntry

```
public SimpleImmutableEntry(Map.Entry<? extends K,? extends V> entry)
```
Creates an entry representing the same mapping as the
specified entry.
Parameters:
`entry` - the entry to copy

### Method Detail

#### getKey

```
public K getKey()
```
Returns the key corresponding to this entry.
Specified by:
`getKey` in interface `Map.Entry<K,V>`
Returns:
the key corresponding to this entry

#### getValue

```
public V getValue()
```
Returns the value corresponding to this entry.
Specified by:
`getValue` in interface `Map.Entry<K,V>`
Returns:
the value corresponding to this entry

#### setValue

```
public V setValue(V value)
```
Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws
UnsupportedOperationException, as this class implements
an immutable map entry.
Specified by:
`setValue` in interface `Map.Entry<K,V>`
Parameters:
`value` - new value to be stored in this entry
Returns:
(Does not return)
Throws:
`UnsupportedOperationException` - always

#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this entry for equality.
Returns `true` if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries `e1` and `e2` represent the same mapping
if
```

   (e1.getKey()==null ?
    e2.getKey()==null :
    e1.getKey().equals(e2.getKey()))
   &&
   (e1.getValue()==null ?
    e2.getValue()==null :
    e1.getValue().equals(e2.getValue()))
```
This ensures that the `equals` method works properly across
different implementations of the `Map.Entry` interface.
Specified by:
`equals` in interface `Map.Entry<K,V>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - object to be compared for equality with this map entry
Returns:
`true` if the specified object is equal to this map
entry
See Also:
`hashCode()`

#### hashCode

```
public int hashCode()
```
Returns the hash code value for this map entry. The hash code
of a map entry `e` is defined to be:
```

   (e.getKey()==null   ? 0 : e.getKey().hashCode()) ^
   (e.getValue()==null ? 0 : e.getValue().hashCode())
```
This ensures that `e1.equals(e2)` implies that
`e1.hashCode()==e2.hashCode()` for any two Entries
`e1` and `e2`, as required by the general
contract of `Object.hashCode()`.
Specified by:
`hashCode` in interface `Map.Entry<K,V>`
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this map entry
See Also:
`equals(java.lang.Object)`

#### toString

```
public String toString()
```
Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("=")
followed by the string representation of this entry's value.
Overrides:
`toString` in class `Object`
Returns:
a String representation of this map entry




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

