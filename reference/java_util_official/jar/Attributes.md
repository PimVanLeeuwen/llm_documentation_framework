

Attributes (Java Platform SE 8 )























<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Attributes (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10,"i9":10,"i10":10,"i11":10,"i12":10,"i13":10,"i14":10,"i15":10,"i16":10,"i17":10};
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
java.util.jarClass Attributes
java.lang.Objectjava.util.jar.Attributes
All Implemented Interfaces:
Cloneable, Map<Object,Object>


```
public class Attributes
extends Object
implements Map<Object,Object>, Cloneable
```
The Attributes class maps Manifest attribute names to associated string
values. Valid attribute names are case-insensitive, are restricted to
the ASCII characters in the set [0-9a-zA-Z\_-], and cannot exceed 70
characters in length. Attribute values can contain any characters and
will be UTF8-encoded when written to the output stream. See the
JAR File Specification
for more information about valid attribute names and values.
Since:
1.2
See Also:
`Manifest`

### Nested Class Summary

Nested Classes Modifier and TypeClass and Description`static class``Attributes.Name`
The Attributes.Name class represents an attribute name stored in
this Map.

### Nested classes/interfaces inherited from interface java.util.Map

`Map.Entry<K,V>`

### Field Summary

Fields Modifier and TypeField and Description`protected Map<Object,Object>``map`
The attribute name-value mappings.

### Constructor Summary

Constructors Constructor and Description`Attributes()`
Constructs a new, empty Attributes object with default size.`Attributes(Attributes attr)`
Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.`Attributes(int size)`
Constructs a new, empty Attributes object with the specified
initial size.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``clear()`
Removes all attributes from this Map.`Object``clone()`
Returns a copy of the Attributes, implemented as follows:`boolean``containsKey(Object name)`
Returns true if this Map contains the specified attribute name (key).`boolean``containsValue(Object value)`
Returns true if this Map maps one or more attribute names (keys)
to the specified value.`Set<Map.Entry<Object,Object>>``entrySet()`
Returns a Collection view of the attribute name-value mappings
contained in this Map.`boolean``equals(Object o)`
Compares the specified Attributes object with this Map for equality.`Object``get(Object name)`
Returns the value of the specified attribute name, or null if the
attribute name was not found.`String``getValue(Attributes.Name name)`
Returns the value of the specified Attributes.Name, or null if the
attribute was not found.`String``getValue(String name)`
Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found.`int``hashCode()`
Returns the hash code value for this Map.`boolean``isEmpty()`
Returns true if this Map contains no attributes.`Set<Object>``keySet()`
Returns a Set view of the attribute names (keys) contained in this Map.`Object``put(Object name,
Object value)`
Associates the specified value with the specified attribute name
(key) in this Map.`void``putAll(Map<?,?> attr)`
Copies all of the attribute name-value mappings from the specified
Attributes to this Map.`String``putValue(String name,
String value)`
Associates the specified value with the specified attribute name,
specified as a String.`Object``remove(Object name)`
Removes the attribute with the specified name (key) from this Map.`int``size()`
Returns the number of attributes in this Map.`Collection<Object>``values()`
Returns a Collection view of the attribute values contained in this Map.

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface java.util.Map

`compute, computeIfAbsent, computeIfPresent, forEach, getOrDefault, merge, putIfAbsent, remove, replace, replace, replaceAll`

### Field Detail

#### map

```
protected Map<Object,Object> map
```
The attribute name-value mappings.

### Constructor Detail

#### Attributes

```
public Attributes()
```
Constructs a new, empty Attributes object with default size.

#### Attributes

```
public Attributes(int size)
```
Constructs a new, empty Attributes object with the specified
initial size.
Parameters:
`size` - the initial number of attributes

#### Attributes

```
public Attributes(Attributes attr)
```
Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.
Parameters:
`attr` - the specified Attributes

### Method Detail

#### get

```
public Object get(Object name)
```
Returns the value of the specified attribute name, or null if the
attribute name was not found.
Specified by:
`get` in interface `Map<Object,Object>`
Parameters:
`name` - the attribute name
Returns:
the value of the specified attribute name, or null if
not found.

#### getValue

```
public String getValue(String name)
```
Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.This method is defined as:
```

      return (String)get(new Attributes.Name((String)name));
 
```

Parameters:
`name` - the attribute name as a string
Returns:
the String value of the specified attribute name, or null if
not found.
Throws:
`IllegalArgumentException` - if the attribute name is invalid

#### getValue

```
public String getValue(Attributes.Name name)
```
Returns the value of the specified Attributes.Name, or null if the
attribute was not found.This method is defined as:
```

     return (String)get(name);
 
```

Parameters:
`name` - the Attributes.Name object
Returns:
the String value of the specified Attribute.Name, or null if
not found.

#### put

```
public Object put(Object name,
                  Object value)
```
Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.
Specified by:
`put` in interface `Map<Object,Object>`
Parameters:
`name` - the attribute name
`value` - the attribute value
Returns:
the previous value of the attribute, or null if none
Throws:
`ClassCastException` - if the name is not a Attributes.Name
or the value is not a String

#### putValue

```
public String putValue(String name,
                       String value)
```
Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.This method is defined as:
```

      return (String)put(new Attributes.Name(name), value);
 
```

Parameters:
`name` - the attribute name as a string
`value` - the attribute value
Returns:
the previous value of the attribute, or null if none
Throws:
`IllegalArgumentException` - if the attribute name is invalid

#### remove

```
public Object remove(Object name)
```
Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.
Specified by:
`remove` in interface `Map<Object,Object>`
Parameters:
`name` - attribute name
Returns:
the previous value of the attribute, or null if none

#### containsValue

```
public boolean containsValue(Object value)
```
Returns true if this Map maps one or more attribute names (keys)
to the specified value.
Specified by:
`containsValue` in interface `Map<Object,Object>`
Parameters:
`value` - the attribute value
Returns:
true if this Map maps one or more attribute names to
the specified value

#### containsKey

```
public boolean containsKey(Object name)
```
Returns true if this Map contains the specified attribute name (key).
Specified by:
`containsKey` in interface `Map<Object,Object>`
Parameters:
`name` - the attribute name
Returns:
true if this Map contains the specified attribute name

#### putAll

```
public void putAll(Map<?,?> attr)
```
Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.
Specified by:
`putAll` in interface `Map<Object,Object>`
Parameters:
`attr` - the Attributes to be stored in this map
Throws:
`ClassCastException` - if attr is not an Attributes

#### clear

```
public void clear()
```
Removes all attributes from this Map.
Specified by:
`clear` in interface `Map<Object,Object>`

#### size

```
public int size()
```
Returns the number of attributes in this Map.
Specified by:
`size` in interface `Map<Object,Object>`
Returns:
the number of key-value mappings in this map

#### isEmpty

```
public boolean isEmpty()
```
Returns true if this Map contains no attributes.
Specified by:
`isEmpty` in interface `Map<Object,Object>`
Returns:
true if this map contains no key-value mappings

#### keySet

```
public Set<Object> keySet()
```
Returns a Set view of the attribute names (keys) contained in this Map.
Specified by:
`keySet` in interface `Map<Object,Object>`
Returns:
a set view of the keys contained in this map

#### values

```
public Collection<Object> values()
```
Returns a Collection view of the attribute values contained in this Map.
Specified by:
`values` in interface `Map<Object,Object>`
Returns:
a collection view of the values contained in this map

#### entrySet

```
public Set<Map.Entry<Object,Object>> entrySet()
```
Returns a Collection view of the attribute name-value mappings
contained in this Map.
Specified by:
`entrySet` in interface `Map<Object,Object>`
Returns:
a set view of the mappings contained in this map

#### equals

```
public boolean equals(Object o)
```
Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.
Specified by:
`equals` in interface `Map<Object,Object>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - the Object to be compared
Returns:
true if the specified Object is equal to this Map
See Also:
`Object.hashCode()`,
`HashMap`

#### hashCode

```
public int hashCode()
```
Returns the hash code value for this Map.
Specified by:
`hashCode` in interface `Map<Object,Object>`
Overrides:
`hashCode` in class `Object`
Returns:
a hash code value for this object.
See Also:
`Object.equals(java.lang.Object)`,
`System.identityHashCode(java.lang.Object)`

#### clone

```
public Object clone()
```
Returns a copy of the Attributes, implemented as follows:
```

     public Object clone() { return new Attributes(this); }
 
```
Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.
Overrides:
`clone` in class `Object`
Returns:
a clone of this instance.
See Also:
`Cloneable`




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

