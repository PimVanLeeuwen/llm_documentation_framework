

Manifest (Java Platform SE 8 )














<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Manifest (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10};
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
java.util.jarClass Manifest
java.lang.Objectjava.util.jar.Manifest
All Implemented Interfaces:
Cloneable


```
public class Manifest
extends Object
implements Cloneable
```
The Manifest class is used to maintain Manifest entry names and their
associated Attributes. There are main Manifest Attributes as well as
per-entry Attributes. For information on the Manifest format, please
see the
Manifest format specification.
Since:
1.2
See Also:
`Attributes`

### Constructor Summary

Constructors Constructor and Description`Manifest()`
Constructs a new, empty Manifest.`Manifest(InputStream is)`
Constructs a new Manifest from the specified input stream.`Manifest(Manifest man)`
Constructs a new Manifest that is a copy of the specified Manifest.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``clear()`
Clears the main Attributes as well as the entries in this Manifest.`Object``clone()`
Returns a shallow copy of this Manifest.`boolean``equals(Object o)`
Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.`Attributes``getAttributes(String name)`
Returns the Attributes for the specified entry name.`Map<String,Attributes>``getEntries()`
Returns a Map of the entries contained in this Manifest.`Attributes``getMainAttributes()`
Returns the main Attributes for the Manifest.`int``hashCode()`
Returns the hash code for this Manifest.`void``read(InputStream is)`
Reads the Manifest from the specified InputStream.`void``write(OutputStream out)`
Writes the Manifest to the specified OutputStream.

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### Manifest

```
public Manifest()
```
Constructs a new, empty Manifest.

#### Manifest

```
public Manifest(InputStream is)
         throws IOException
```
Constructs a new Manifest from the specified input stream.
Parameters:
`is` - the input stream containing manifest data
Throws:
`IOException` - if an I/O error has occurred

#### Manifest

```
public Manifest(Manifest man)
```
Constructs a new Manifest that is a copy of the specified Manifest.
Parameters:
`man` - the Manifest to copy

### Method Detail

#### getMainAttributes

```
public Attributes getMainAttributes()
```
Returns the main Attributes for the Manifest.
Returns:
the main Attributes for the Manifest

#### getEntries

```
public Map<String,Attributes> getEntries()
```
Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the `null` key, but no entry with a null key is
created by `read(java.io.InputStream)`, nor is such an entry written by using `write(java.io.OutputStream)`.
Returns:
a Map of the entries contained in this Manifest

#### getAttributes

```
public Attributes getAttributes(String name)
```
Returns the Attributes for the specified entry name.
This method is defined as:
```

      return (Attributes)getEntries().get(name)
 
```
Though `null` is a valid `name`, when
`getAttributes(null)` is invoked on a `Manifest`
obtained from a jar file, `null` will be returned. While jar
files themselves do not allow `null`-named attributes, it is
possible to invoke `getEntries()` on a `Manifest`, and
on that result, invoke `put` with a null key and an
arbitrary value. Subsequent invocations of
`getAttributes(null)` will return the just-`put`
value.Note that this method does not return the manifest's main attributes;
see `getMainAttributes()`.
Parameters:
`name` - entry name
Returns:
the Attributes for the specified entry name

#### clear

```
public void clear()
```
Clears the main Attributes as well as the entries in this Manifest.

#### write

```
public void write(OutputStream out)
           throws IOException
```
Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST\_VERSION must be set in
MainAttributes prior to invoking this method.
Parameters:
`out` - the output stream
Throws:
`IOException` - if an I/O error has occurred
See Also:
`getMainAttributes()`

#### read

```
public void read(InputStream is)
          throws IOException
```
Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.
Parameters:
`is` - the input stream
Throws:
`IOException` - if an I/O error has occurred

#### equals

```
public boolean equals(Object o)
```
Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.
Overrides:
`equals` in class `Object`
Parameters:
`o` - the object to be compared
Returns:
true if the specified Object is also a Manifest and has
the same main Attributes and entries
See Also:
`Object.hashCode()`,
`HashMap`

#### hashCode

```
public int hashCode()
```
Returns the hash code for this Manifest.
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
Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:
```

     public Object clone() { return new Manifest(this); }
 
```

Overrides:
`clone` in class `Object`
Returns:
a shallow copy of this Manifest
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

