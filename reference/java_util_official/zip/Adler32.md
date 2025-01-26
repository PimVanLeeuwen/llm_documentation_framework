

Adler32 (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Adler32 (Java Platform SE 8 )";
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
java.util.zipClass Adler32
java.lang.Objectjava.util.zip.Adler32
All Implemented Interfaces:
Checksum


```
public class Adler32
extends Object
implements Checksum
```
A class that can be used to compute the Adler-32 checksum of a data
stream. An Adler-32 checksum is almost as reliable as a CRC-32 but
can be computed much faster.Passing a `null` argument to a method in this class will cause
a `NullPointerException` to be thrown.
See Also:
`Checksum`

### Constructor Summary

Constructors Constructor and Description`Adler32()`
Creates a new Adler32 object.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`long``getValue()`
Returns the checksum value.`void``reset()`
Resets the checksum to initial value.`void``update(byte[] b)`
Updates the checksum with the specified array of bytes.`void``update(byte[] b,
int off,
int len)`
Updates the checksum with the specified array of bytes.`void``update(ByteBuffer buffer)`
Updates the checksum with the bytes from the specified buffer.`void``update(int b)`
Updates the checksum with the specified byte (the low eight
bits of the argument b).

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### Adler32

```
public Adler32()
```
Creates a new Adler32 object.

### Method Detail

#### update

```
public void update(int b)
```
Updates the checksum with the specified byte (the low eight
bits of the argument b).
Specified by:
`update` in interface `Checksum`
Parameters:
`b` - the byte to update the checksum with

#### update

```
public void update(byte[] b,
                   int off,
                   int len)
```
Updates the checksum with the specified array of bytes.
Specified by:
`update` in interface `Checksum`
Parameters:
`b` - the byte array to update the checksum with
`off` - the start offset of the data
`len` - the number of bytes to use for the update
Throws:
`ArrayIndexOutOfBoundsException` - if `off` is negative, or `len` is negative,
or `off+len` is greater than the length of the
array `b`

#### update

```
public void update(byte[] b)
```
Updates the checksum with the specified array of bytes.
Parameters:
`b` - the byte array to update the checksum with

#### update

```
public void update(ByteBuffer buffer)
```
Updates the checksum with the bytes from the specified buffer.
The checksum is updated using
buffer.`remaining()`
bytes starting at
buffer.`position()`
Upon return, the buffer's position will be updated to its
limit; its limit will not have been changed.
Parameters:
`buffer` - the ByteBuffer to update the checksum with
Since:
1.8

#### reset

```
public void reset()
```
Resets the checksum to initial value.
Specified by:
`reset` in interface `Checksum`

#### getValue

```
public long getValue()
```
Returns the checksum value.
Specified by:
`getValue` in interface `Checksum`
Returns:
the current checksum value




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

