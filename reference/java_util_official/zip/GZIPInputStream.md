

GZIPInputStream (Java Platform SE 8 )










<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="GZIPInputStream (Java Platform SE 8 )";
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
java.util.zipClass GZIPInputStream
java.lang.Objectjava.io.InputStreamjava.io.FilterInputStreamjava.util.zip.InflaterInputStreamjava.util.zip.GZIPInputStream
All Implemented Interfaces:
Closeable, AutoCloseable


```
public class GZIPInputStream
extends InflaterInputStream
```
This class implements a stream filter for reading compressed data in
the GZIP file format.
See Also:
`InflaterInputStream`

### Field Summary

Fields Modifier and TypeField and Description`protected CRC32``crc`
CRC-32 for uncompressed data.`protected boolean``eos`
Indicates end of input stream.`static int``GZIP_MAGIC`
GZIP header magic number.

### Fields inherited from class java.util.zip.InflaterInputStream

`buf, inf, len`

### Fields inherited from class java.io.FilterInputStream

`in`

### Constructor Summary

Constructors Constructor and Description`GZIPInputStream(InputStream in)`
Creates a new input stream with a default buffer size.`GZIPInputStream(InputStream in,
int size)`
Creates a new input stream with the specified buffer size.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``close()`
Closes this input stream and releases any system resources associated
with the stream.`int``read(byte[] buf,
int off,
int len)`
Reads uncompressed data into an array of bytes.

### Methods inherited from class java.util.zip.InflaterInputStream

`available, fill, mark, markSupported, read, reset, skip`

### Methods inherited from class java.io.FilterInputStream

`read`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### crc

```
protected CRC32 crc
```
CRC-32 for uncompressed data.

#### eos

```
protected boolean eos
```
Indicates end of input stream.

#### GZIP\_MAGIC

```
public static final int GZIP_MAGIC
```
GZIP header magic number.
See Also:
Constant Field Values

### Constructor Detail

#### GZIPInputStream

```
public GZIPInputStream(InputStream in,
                       int size)
                throws IOException
```
Creates a new input stream with the specified buffer size.
Parameters:
`in` - the input stream
`size` - the input buffer size
Throws:
`ZipException` - if a GZIP format error has occurred or the
compression method used is unsupported
`IOException` - if an I/O error has occurred
`IllegalArgumentException` - if `size <= 0`

#### GZIPInputStream

```
public GZIPInputStream(InputStream in)
                throws IOException
```
Creates a new input stream with a default buffer size.
Parameters:
`in` - the input stream
Throws:
`ZipException` - if a GZIP format error has occurred or the
compression method used is unsupported
`IOException` - if an I/O error has occurred

### Method Detail

#### read

```
public int read(byte[] buf,
                int off,
                int len)
         throws IOException
```
Reads uncompressed data into an array of bytes. If `len` is not
zero, the method will block until some input can be decompressed; otherwise,
no bytes are read and `0` is returned.
Overrides:
`read` in class `InflaterInputStream`
Parameters:
`buf` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end of the
compressed input stream is reached
Throws:
`NullPointerException` - If `buf` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`buf.length - off`
`ZipException` - if the compressed input data is corrupt.
`IOException` - if an I/O error has occurred.
See Also:
`FilterInputStream.in`

#### close

```
public void close()
           throws IOException
```
Closes this input stream and releases any system resources associated
with the stream.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `InflaterInputStream`
Throws:
`IOException` - if an I/O error has occurred
See Also:
`FilterInputStream.in`




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

