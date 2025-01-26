

GZIPOutputStream (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="GZIPOutputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10};
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
java.util.zipClass GZIPOutputStream
java.lang.Objectjava.io.OutputStreamjava.io.FilterOutputStreamjava.util.zip.DeflaterOutputStreamjava.util.zip.GZIPOutputStream
All Implemented Interfaces:
Closeable, Flushable, AutoCloseable


```
public class GZIPOutputStream
extends DeflaterOutputStream
```
This class implements a stream filter for writing compressed data in
the GZIP file format.

### Field Summary

Fields Modifier and TypeField and Description`protected CRC32``crc`
CRC-32 of uncompressed data.

### Fields inherited from class java.util.zip.DeflaterOutputStream

`buf, def`

### Fields inherited from class java.io.FilterOutputStream

`out`

### Constructor Summary

Constructors Constructor and Description`GZIPOutputStream(OutputStream out)`
Creates a new output stream with a default buffer size.`GZIPOutputStream(OutputStream out,
boolean syncFlush)`
Creates a new output stream with a default buffer size and
the specified flush mode.`GZIPOutputStream(OutputStream out,
int size)`
Creates a new output stream with the specified buffer size.`GZIPOutputStream(OutputStream out,
int size,
boolean syncFlush)`
Creates a new output stream with the specified buffer size and
flush mode.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``finish()`
Finishes writing compressed data to the output stream without closing
the underlying stream.`void``write(byte[] buf,
int off,
int len)`
Writes array of bytes to the compressed output stream.

### Methods inherited from class java.util.zip.DeflaterOutputStream

`close, deflate, flush, write`

### Methods inherited from class java.io.FilterOutputStream

`write`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### crc

```
protected CRC32 crc
```
CRC-32 of uncompressed data.

### Constructor Detail

#### GZIPOutputStream

```
public GZIPOutputStream(OutputStream out,
                        int size)
                 throws IOException
```
Creates a new output stream with the specified buffer size.The new output stream instance is created as if by invoking
the 3-argument constructor GZIPOutputStream(out, size, false).
Parameters:
`out` - the output stream
`size` - the output buffer size
Throws:
`IOException` - If an I/O error has occurred.
`IllegalArgumentException` - if `size <= 0`

#### GZIPOutputStream

```
public GZIPOutputStream(OutputStream out,
                        int size,
                        boolean syncFlush)
                 throws IOException
```
Creates a new output stream with the specified buffer size and
flush mode.
Parameters:
`out` - the output stream
`size` - the output buffer size
`syncFlush` - if `true` invocation of the inherited
`flush()` method of
this instance flushes the compressor with flush mode
`Deflater.SYNC_FLUSH` before flushing the output
stream, otherwise only flushes the output stream
Throws:
`IOException` - If an I/O error has occurred.
`IllegalArgumentException` - if `size <= 0`
Since:
1.7

#### GZIPOutputStream

```
public GZIPOutputStream(OutputStream out)
                 throws IOException
```
Creates a new output stream with a default buffer size.The new output stream instance is created as if by invoking
the 2-argument constructor GZIPOutputStream(out, false).
Parameters:
`out` - the output stream
Throws:
`IOException` - If an I/O error has occurred.

#### GZIPOutputStream

```
public GZIPOutputStream(OutputStream out,
                        boolean syncFlush)
                 throws IOException
```
Creates a new output stream with a default buffer size and
the specified flush mode.
Parameters:
`out` - the output stream
`syncFlush` - if `true` invocation of the inherited
`flush()` method of
this instance flushes the compressor with flush mode
`Deflater.SYNC_FLUSH` before flushing the output
stream, otherwise only flushes the output stream
Throws:
`IOException` - If an I/O error has occurred.
Since:
1.7

### Method Detail

#### write

```
public void write(byte[] buf,
                  int off,
                  int len)
           throws IOException
```
Writes array of bytes to the compressed output stream. This method
will block until all the bytes are written.
Overrides:
`write` in class `DeflaterOutputStream`
Parameters:
`buf` - the data to be written
`off` - the start offset of the data
`len` - the length of the data
Throws:
`IOException` - If an I/O error has occurred.
See Also:
`FilterOutputStream.write(int)`

#### finish

```
public void finish()
            throws IOException
```
Finishes writing compressed data to the output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.
Overrides:
`finish` in class `DeflaterOutputStream`
Throws:
`IOException` - if an I/O error has occurred




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

