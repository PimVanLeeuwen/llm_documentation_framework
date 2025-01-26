

Dictionary (Java Platform SE 8 )












<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Dictionary (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6,"i2":6,"i3":6,"i4":6,"i5":6,"i6":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
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
java.utilClass Dictionary<K,V>
java.lang.Objectjava.util.Dictionary<K,V>
Direct Known Subclasses:
Hashtable


```
public abstract class Dictionary<K,V>
extends Object
```
The `Dictionary` class is the abstract parent of any
class, such as `Hashtable`, which maps keys to values.
Every key and every value is an object. In any one Dictionary
object, every key is associated with at most one value. Given a
Dictionary and a key, the associated element can be looked up.
Any non-`null` object can be used as a key and as a value.As a rule, the `equals` method should be used by
implementations of this class to decide if two keys are the same.NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.
Since:
JDK1.0
See Also:
`Map`,
`Object.equals(java.lang.Object)`,
`Object.hashCode()`,
`Hashtable`

### Constructor Summary

Constructors Constructor and Description`Dictionary()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`abstract Enumeration<V>``elements()`
Returns an enumeration of the values in this dictionary.`abstract V``get(Object key)`
Returns the value to which the key is mapped in this dictionary.`abstract boolean``isEmpty()`
Tests if this dictionary maps no keys to value.`abstract Enumeration<K>``keys()`
Returns an enumeration of the keys in this dictionary.`abstract V``put(K key,
V value)`
Maps the specified `key` to the specified
`value` in this dictionary.`abstract V``remove(Object key)`
Removes the `key` (and its corresponding
`value`) from this dictionary.`abstract int``size()`
Returns the number of entries (distinct keys) in this dictionary.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### Dictionary

```
public Dictionary()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### size

```
public abstract int size()
```
Returns the number of entries (distinct keys) in this dictionary.
Returns:
the number of keys in this dictionary.

#### isEmpty

```
public abstract boolean isEmpty()
```
Tests if this dictionary maps no keys to value. The general contract
for the isEmpty method is that the result is true if and only
if this dictionary contains no entries.
Returns:
`true` if this dictionary maps no keys to values;
`false` otherwise.

#### keys

```
public abstract Enumeration<K> keys()
```
Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an Enumeration object
is returned that will generate all the keys for which this dictionary
contains entries.
Returns:
an enumeration of the keys in this dictionary.
See Also:
`elements()`,
`Enumeration`

#### elements

```
public abstract Enumeration<V> elements()
```
Returns an enumeration of the values in this dictionary. The general
contract for the elements method is that an
Enumeration is returned that will generate all the elements
contained in entries in this dictionary.
Returns:
an enumeration of the values in this dictionary.
See Also:
`keys()`,
`Enumeration`

#### get

```
public abstract V get(Object key)
```
Returns the value to which the key is mapped in this dictionary.
The general contract for the isEmpty method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise, null is returned.
Parameters:
`key` - a key in this dictionary.
`null` if the key is not mapped to any value in
this dictionary.
Returns:
the value to which the key is mapped in this dictionary;
Throws:
`NullPointerException` - if the key is null.
See Also:
`put(java.lang.Object, java.lang.Object)`

#### put

```
public abstract V put(K key,
                      V value)
```
Maps the specified `key` to the specified
`value` in this dictionary. Neither the key nor the
value can be `null`.If this dictionary already contains an entry for the specified
key, the value already in this dictionary for that
key is returned, after modifying the entry to contain the
new element.If this dictionary does not already have an entry
for the specified key, an entry is created for the
specified key and value, and null is
returned.The `value` can be retrieved by calling the
`get` method with a `key` that is equal to
the original `key`.
Parameters:
`key` - the hashtable key.
`value` - the value.
Returns:
the previous value to which the `key` was mapped
in this dictionary, or `null` if the key did not
have a previous mapping.
Throws:
`NullPointerException` - if the `key` or
`value` is `null`.
See Also:
`Object.equals(java.lang.Object)`,
`get(java.lang.Object)`

#### remove

```
public abstract V remove(Object key)
```
Removes the `key` (and its corresponding
`value`) from this dictionary. This method does nothing
if the `key` is not in this dictionary.
Parameters:
`key` - the key that needs to be removed.
Returns:
the value to which the `key` had been mapped in this
dictionary, or `null` if the key did not have a
mapping.
Throws:
`NullPointerException` - if key is null.




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

