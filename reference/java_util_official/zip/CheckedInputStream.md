

CheckedInputStream (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="CheckedInputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10};
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
java.util.zipClass CheckedInputStream
java.lang.Objectjava.io.InputStreamjava.io.FilterInputStreamjava.util.zip.CheckedInputStream
All Implemented Interfaces:
Closeable, AutoCloseable


```
public class CheckedInputStream
extends FilterInputStream
```
An input stream that also maintains a checksum of the data being read.
The checksum can then be used to verify the integrity of the input data.
See Also:
`Checksum`

### Field Summary

### Fields inherited from class java.io.FilterInputStream

`in`

### Constructor Summary

Constructors Constructor and Description`CheckedInputStream(InputStream in,
Checksum cksum)`
Creates an input stream using the specified Checksum.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Checksum``getChecksum()`
Returns the Checksum for this input stream.`int``read()`
Reads a byte.`int``read(byte[] buf,
int off,
int len)`
Reads into an array of bytes.`long``skip(long n)`
Skips specified number of bytes of input.

### Methods inherited from class java.io.FilterInputStream

`available, close, mark, markSupported, read, reset`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### CheckedInputStream

```
public CheckedInputStream(InputStream in,
                          Checksum cksum)
```
Creates an input stream using the specified Checksum.
Parameters:
`in` - the input stream
`cksum` - the Checksum

### Method Detail

#### read

```
public int read()
         throws IOException
```
Reads a byte. Will block if no input is available.
Overrides:
`read` in class `FilterInputStream`
Returns:
the byte read, or -1 if the end of the stream is reached.
Throws:
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`

#### read

```
public int read(byte[] buf,
                int off,
                int len)
         throws IOException
```
Reads into an array of bytes. If `len` is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and `0` is returned.
Overrides:
`read` in class `FilterInputStream`
Parameters:
`buf` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end
of the stream is reached.
Throws:
`NullPointerException` - If `buf` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`buf.length - off`
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`

#### skip

```
public long skip(long n)
          throws IOException
```
Skips specified number of bytes of input.
Overrides:
`skip` in class `FilterInputStream`
Parameters:
`n` - the number of bytes to skip
Returns:
the actual number of bytes skipped
Throws:
`IOException` - if an I/O error has occurred

#### getChecksum

```
public Checksum getChecksum()
```
Returns the Checksum for this input stream.
Returns:
the Checksum value




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

