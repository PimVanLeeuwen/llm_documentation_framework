

CheckedOutputStream (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="CheckedOutputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10};
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
java.util.zipClass CheckedOutputStream
java.lang.Objectjava.io.OutputStreamjava.io.FilterOutputStreamjava.util.zip.CheckedOutputStream
All Implemented Interfaces:
Closeable, Flushable, AutoCloseable


```
public class CheckedOutputStream
extends FilterOutputStream
```
An output stream that also maintains a checksum of the data being
written. The checksum can then be used to verify the integrity of
the output data.
See Also:
`Checksum`

### Field Summary

### Fields inherited from class java.io.FilterOutputStream

`out`

### Constructor Summary

Constructors Constructor and Description`CheckedOutputStream(OutputStream out,
Checksum cksum)`
Creates an output stream with the specified Checksum.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Checksum``getChecksum()`
Returns the Checksum for this output stream.`void``write(byte[] b,
int off,
int len)`
Writes an array of bytes.`void``write(int b)`
Writes a byte.

### Methods inherited from class java.io.FilterOutputStream

`close, flush, write`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### CheckedOutputStream

```
public CheckedOutputStream(OutputStream out,
                           Checksum cksum)
```
Creates an output stream with the specified Checksum.
Parameters:
`out` - the output stream
`cksum` - the checksum

### Method Detail

#### write

```
public void write(int b)
           throws IOException
```
Writes a byte. Will block until the byte is actually written.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the byte to be written
Throws:
`IOException` - if an I/O error has occurred

#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes. Will block until the bytes are
actually written.
Overrides:
`write` in class `FilterOutputStream`
Parameters:
`b` - the data to be written
`off` - the start offset of the data
`len` - the number of bytes to be written
Throws:
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.write(int)`

#### getChecksum

```
public Checksum getChecksum()
```
Returns the Checksum for this output stream.
Returns:
the Checksum




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

