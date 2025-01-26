

ZipOutputStream (Java Platform SE 8 )















<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ZipOutputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10};
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
java.util.zipClass ZipOutputStream
java.lang.Objectjava.io.OutputStreamjava.io.FilterOutputStreamjava.util.zip.DeflaterOutputStreamjava.util.zip.ZipOutputStream
All Implemented Interfaces:
Closeable, Flushable, AutoCloseable

Direct Known Subclasses:
JarOutputStream


```
public class ZipOutputStream
extends DeflaterOutputStream
```
This class implements an output stream filter for writing files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``DEFLATED`
Compression method for compressed (DEFLATED) entries.`static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER``static int``STORED`
Compression method for uncompressed (STORED) entries.

### Fields inherited from class java.util.zip.DeflaterOutputStream

`buf, def`

### Fields inherited from class java.io.FilterOutputStream

`out`

### Constructor Summary

Constructors Constructor and Description`ZipOutputStream(OutputStream out)`
Creates a new ZIP output stream.`ZipOutputStream(OutputStream out,
Charset charset)`
Creates a new ZIP output stream.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``close()`
Closes the ZIP output stream as well as the stream being filtered.`void``closeEntry()`
Closes the current ZIP entry and positions the stream for writing
the next entry.`void``finish()`
Finishes writing the contents of the ZIP output stream without closing
the underlying stream.`void``putNextEntry(ZipEntry e)`
Begins writing a new ZIP file entry and positions the stream to the
start of the entry data.`void``setComment(String comment)`
Sets the ZIP file comment.`void``setLevel(int level)`
Sets the compression level for subsequent entries which are DEFLATED.`void``setMethod(int method)`
Sets the default compression method for subsequent entries.`void``write(byte[] b,
int off,
int len)`
Writes an array of bytes to the current ZIP entry data.

### Methods inherited from class java.util.zip.DeflaterOutputStream

`deflate, flush, write`

### Methods inherited from class java.io.FilterOutputStream

`write`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### STORED

```
public static final int STORED
```
Compression method for uncompressed (STORED) entries.
See Also:
Constant Field Values

#### DEFLATED

```
public static final int DEFLATED
```
Compression method for compressed (DEFLATED) entries.
See Also:
Constant Field Values

#### LOCSIG

```
public static final long LOCSIG
```
See Also:
Constant Field Values

#### EXTSIG

```
public static final long EXTSIG
```
See Also:
Constant Field Values

#### CENSIG

```
public static final long CENSIG
```
See Also:
Constant Field Values

#### ENDSIG

```
public static final long ENDSIG
```
See Also:
Constant Field Values

#### LOCHDR

```
public static final int LOCHDR
```
See Also:
Constant Field Values

#### EXTHDR

```
public static final int EXTHDR
```
See Also:
Constant Field Values

#### CENHDR

```
public static final int CENHDR
```
See Also:
Constant Field Values

#### ENDHDR

```
public static final int ENDHDR
```
See Also:
Constant Field Values

#### LOCVER

```
public static final int LOCVER
```
See Also:
Constant Field Values

#### LOCFLG

```
public static final int LOCFLG
```
See Also:
Constant Field Values

#### LOCHOW

```
public static final int LOCHOW
```
See Also:
Constant Field Values

#### LOCTIM

```
public static final int LOCTIM
```
See Also:
Constant Field Values

#### LOCCRC

```
public static final int LOCCRC
```
See Also:
Constant Field Values

#### LOCSIZ

```
public static final int LOCSIZ
```
See Also:
Constant Field Values

#### LOCLEN

```
public static final int LOCLEN
```
See Also:
Constant Field Values

#### LOCNAM

```
public static final int LOCNAM
```
See Also:
Constant Field Values

#### LOCEXT

```
public static final int LOCEXT
```
See Also:
Constant Field Values

#### EXTCRC

```
public static final int EXTCRC
```
See Also:
Constant Field Values

#### EXTSIZ

```
public static final int EXTSIZ
```
See Also:
Constant Field Values

#### EXTLEN

```
public static final int EXTLEN
```
See Also:
Constant Field Values

#### CENVEM

```
public static final int CENVEM
```
See Also:
Constant Field Values

#### CENVER

```
public static final int CENVER
```
See Also:
Constant Field Values

#### CENFLG

```
public static final int CENFLG
```
See Also:
Constant Field Values

#### CENHOW

```
public static final int CENHOW
```
See Also:
Constant Field Values

#### CENTIM

```
public static final int CENTIM
```
See Also:
Constant Field Values

#### CENCRC

```
public static final int CENCRC
```
See Also:
Constant Field Values

#### CENSIZ

```
public static final int CENSIZ
```
See Also:
Constant Field Values

#### CENLEN

```
public static final int CENLEN
```
See Also:
Constant Field Values

#### CENNAM

```
public static final int CENNAM
```
See Also:
Constant Field Values

#### CENEXT

```
public static final int CENEXT
```
See Also:
Constant Field Values

#### CENCOM

```
public static final int CENCOM
```
See Also:
Constant Field Values

#### CENDSK

```
public static final int CENDSK
```
See Also:
Constant Field Values

#### CENATT

```
public static final int CENATT
```
See Also:
Constant Field Values

#### CENATX

```
public static final int CENATX
```
See Also:
Constant Field Values

#### CENOFF

```
public static final int CENOFF
```
See Also:
Constant Field Values

#### ENDSUB

```
public static final int ENDSUB
```
See Also:
Constant Field Values

#### ENDTOT

```
public static final int ENDTOT
```
See Also:
Constant Field Values

#### ENDSIZ

```
public static final int ENDSIZ
```
See Also:
Constant Field Values

#### ENDOFF

```
public static final int ENDOFF
```
See Also:
Constant Field Values

#### ENDCOM

```
public static final int ENDCOM
```
See Also:
Constant Field Values

### Constructor Detail

#### ZipOutputStream

```
public ZipOutputStream(OutputStream out)
```
Creates a new ZIP output stream.The UTF-8 `charset` is used
to encode the entry names and comments.
Parameters:
`out` - the actual output stream

#### ZipOutputStream

```
public ZipOutputStream(OutputStream out,
                       Charset charset)
```
Creates a new ZIP output stream.
Parameters:
`out` - the actual output stream
`charset` - the charset
to be used to encode the entry names and comments
Since:
1.7

### Method Detail

#### setComment

```
public void setComment(String comment)
```
Sets the ZIP file comment.
Parameters:
`comment` - the comment string
Throws:
`IllegalArgumentException` - if the length of the specified
ZIP file comment is greater than 0xFFFF bytes

#### setMethod

```
public void setMethod(int method)
```
Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.
Parameters:
`method` - the default compression method
Throws:
`IllegalArgumentException` - if the specified compression method
is invalid

#### setLevel

```
public void setLevel(int level)
```
Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT\_COMPRESSION.
Parameters:
`level` - the compression level (0-9)
Throws:
`IllegalArgumentException` - if the compression level is invalid

#### putNextEntry

```
public void putNextEntry(ZipEntry e)
                  throws IOException
```
Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.
Parameters:
`e` - the ZIP entry to be written
Throws:
`ZipException` - if a ZIP format error has occurred
`IOException` - if an I/O error has occurred

#### closeEntry

```
public void closeEntry()
                throws IOException
```
Closes the current ZIP entry and positions the stream for writing
the next entry.
Throws:
`ZipException` - if a ZIP format error has occurred
`IOException` - if an I/O error has occurred

#### write

```
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```
Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.
Overrides:
`write` in class `DeflaterOutputStream`
Parameters:
`b` - the data to be written
`off` - the start offset in the data
`len` - the number of bytes that are written
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.write(int)`

#### finish

```
public void finish()
            throws IOException
```
Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.
Overrides:
`finish` in class `DeflaterOutputStream`
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O exception has occurred

#### close

```
public void close()
           throws IOException
```
Closes the ZIP output stream as well as the stream being filtered.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`
Overrides:
`close` in class `DeflaterOutputStream`
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
See Also:
`FilterOutputStream.flush()`,
`FilterOutputStream.out`




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

