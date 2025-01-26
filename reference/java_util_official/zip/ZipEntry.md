

ZipEntry (Java Platform SE 8 )
































<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ZipEntry (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10,"i9":10,"i10":10,"i11":10,"i12":10,"i13":10,"i14":10,"i15":10,"i16":10,"i17":10,"i18":10,"i19":10,"i20":10,"i21":10,"i22":10,"i23":10,"i24":10};
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
java.util.zipClass ZipEntry
java.lang.Objectjava.util.zip.ZipEntry
All Implemented Interfaces:
Cloneable

Direct Known Subclasses:
JarEntry


```
public class ZipEntry
extends Object
implements Cloneable
```
This class is used to represent a ZIP file entry.

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``DEFLATED`
Compression method for compressed (deflated) entries.`static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER``static int``STORED`
Compression method for uncompressed entries.

### Constructor Summary

Constructors Constructor and Description`ZipEntry(String name)`
Creates a new zip entry with the specified name.`ZipEntry(ZipEntry e)`
Creates a new zip entry with fields taken from the specified
zip entry.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Object``clone()`
Returns a copy of this entry.`String``getComment()`
Returns the comment string for the entry.`long``getCompressedSize()`
Returns the size of the compressed entry data.`long``getCrc()`
Returns the CRC-32 checksum of the uncompressed entry data.`FileTime``getCreationTime()`
Returns the creation time of the entry.`byte[]``getExtra()`
Returns the extra field data for the entry.`FileTime``getLastAccessTime()`
Returns the last access time of the entry.`FileTime``getLastModifiedTime()`
Returns the last modification time of the entry.`int``getMethod()`
Returns the compression method of the entry.`String``getName()`
Returns the name of the entry.`long``getSize()`
Returns the uncompressed size of the entry data.`long``getTime()`
Returns the last modification time of the entry.`int``hashCode()`
Returns the hash code value for this entry.`boolean``isDirectory()`
Returns true if this is a directory entry.`void``setComment(String comment)`
Sets the optional comment string for the entry.`void``setCompressedSize(long csize)`
Sets the size of the compressed entry data.`void``setCrc(long crc)`
Sets the CRC-32 checksum of the uncompressed entry data.`ZipEntry``setCreationTime(FileTime time)`
Sets the creation time of the entry.`void``setExtra(byte[] extra)`
Sets the optional extra field data for the entry.`ZipEntry``setLastAccessTime(FileTime time)`
Sets the last access time of the entry.`ZipEntry``setLastModifiedTime(FileTime time)`
Sets the last modification time of the entry.`void``setMethod(int method)`
Sets the compression method for the entry.`void``setSize(long size)`
Sets the uncompressed size of the entry data.`void``setTime(long time)`
Sets the last modification time of the entry.`String``toString()`
Returns a string representation of the ZIP entry.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Field Detail

#### STORED

```
public static final int STORED
```
Compression method for uncompressed entries.
See Also:
Constant Field Values

#### DEFLATED

```
public static final int DEFLATED
```
Compression method for compressed (deflated) entries.
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

#### ZipEntry

```
public ZipEntry(String name)
```
Creates a new zip entry with the specified name.
Parameters:
`name` - The entry name
Throws:
`NullPointerException` - if the entry name is null
`IllegalArgumentException` - if the entry name is longer than
0xFFFF bytes

#### ZipEntry

```
public ZipEntry(ZipEntry e)
```
Creates a new zip entry with fields taken from the specified
zip entry.
Parameters:
`e` - A zip Entry object
Throws:
`NullPointerException` - if the entry object is null

### Method Detail

#### getName

```
public String getName()
```
Returns the name of the entry.
Returns:
the name of the entry

#### setTime

```
public void setTime(long time)
```
Sets the last modification time of the entry.If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the `date and time fields` of the zip file
entry and encoded in standard `MS-DOS date and time format`.
The `default TimeZone` is
used to convert the epoch time to the MS-DOS data and time.
Parameters:
`time` - The last modification time of the entry in milliseconds
since the epoch
See Also:
`getTime()`,
`getLastModifiedTime()`

#### getTime

```
public long getTime()
```
Returns the last modification time of the entry.If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the `date and time fields` of the zip file entry. The
`default TimeZone` is used
to convert the standard MS-DOS formatted date and time to the
epoch time.
Returns:
The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified
See Also:
`setTime(long)`,
`setLastModifiedTime(FileTime)`

#### setLastModifiedTime

```
public ZipEntry setLastModifiedTime(FileTime time)
```
Sets the last modification time of the entry.When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's `date and time fields` in `standard
MS-DOS date and time format`), and the extended timestamp fields
in `optional extra data` in UTC time.
Parameters:
`time` - The last modification time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getLastModifiedTime()`

#### getLastModifiedTime

```
public FileTime getLastModifiedTime()
```
Returns the last modification time of the entry.If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's `optional extra data` if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's `date and time fields`, the `default TimeZone` is used to convert
the standard MS-DOS formatted date and time to the epoch time.
Returns:
The last modification time of the entry, null if not specified
Since:
1.8
See Also:
`setLastModifiedTime(FileTime)`

#### setLastAccessTime

```
public ZipEntry setLastAccessTime(FileTime time)
```
Sets the last access time of the entry.If set, the last access time will be stored into the extended
timestamp fields of entry's `optional extra data`, when output
to a ZIP file or ZIP file formatted stream.
Parameters:
`time` - The last access time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getLastAccessTime()`

#### getLastAccessTime

```
public FileTime getLastAccessTime()
```
Returns the last access time of the entry.The last access time is from the extended timestamp fields
of entry's `optional extra data` when read from a ZIP file
or ZIP file formatted stream.
Returns:
The last access time of the entry, null if not specified
Since:
1.8
See Also:
`setLastAccessTime(FileTime)`

#### setCreationTime

```
public ZipEntry setCreationTime(FileTime time)
```
Sets the creation time of the entry.If set, the creation time will be stored into the extended
timestamp fields of entry's `optional extra data`, when
output to a ZIP file or ZIP file formatted stream.
Parameters:
`time` - The creation time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getCreationTime()`

#### getCreationTime

```
public FileTime getCreationTime()
```
Returns the creation time of the entry.The creation time is from the extended timestamp fields of
entry's `optional extra data` when read from a ZIP file
or ZIP file formatted stream.
Returns:
the creation time of the entry, null if not specified
Since:
1.8
See Also:
`setCreationTime(FileTime)`

#### setSize

```
public void setSize(long size)
```
Sets the uncompressed size of the entry data.
Parameters:
`size` - the uncompressed size in bytes
Throws:
`IllegalArgumentException` - if the specified size is less
than 0, is greater than 0xFFFFFFFF when
ZIP64 format is not supported,
or is less than 0 when ZIP64 is supported
See Also:
`getSize()`

#### getSize

```
public long getSize()
```
Returns the uncompressed size of the entry data.
Returns:
the uncompressed size of the entry data, or -1 if not known
See Also:
`setSize(long)`

#### getCompressedSize

```
public long getCompressedSize()
```
Returns the size of the compressed entry data.In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.
Returns:
the size of the compressed entry data, or -1 if not known
See Also:
`setCompressedSize(long)`

#### setCompressedSize

```
public void setCompressedSize(long csize)
```
Sets the size of the compressed entry data.
Parameters:
`csize` - the compressed size to set to
See Also:
`getCompressedSize()`

#### setCrc

```
public void setCrc(long crc)
```
Sets the CRC-32 checksum of the uncompressed entry data.
Parameters:
`crc` - the CRC-32 value
Throws:
`IllegalArgumentException` - if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF
See Also:
`getCrc()`

#### getCrc

```
public long getCrc()
```
Returns the CRC-32 checksum of the uncompressed entry data.
Returns:
the CRC-32 checksum of the uncompressed entry data, or -1 if
not known
See Also:
`setCrc(long)`

#### setMethod

```
public void setMethod(int method)
```
Sets the compression method for the entry.
Parameters:
`method` - the compression method, either STORED or DEFLATED
Throws:
`IllegalArgumentException` - if the specified compression
method is invalid
See Also:
`getMethod()`

#### getMethod

```
public int getMethod()
```
Returns the compression method of the entry.
Returns:
the compression method of the entry, or -1 if not specified
See Also:
`setMethod(int)`

#### setExtra

```
public void setExtra(byte[] extra)
```
Sets the optional extra field data for the entry.Invoking this method may change this entry's last modification
time, last access time and creation time, if the `extra` field
data includes the extensible timestamp fields, such as `NTFS tag
0x0001` or `Info-ZIP Extended Timestamp`, as specified in
Info-ZIP
Application Note 970311.
Parameters:
`extra` - The extra field data bytes
Throws:
`IllegalArgumentException` - if the length of the specified
extra field data is greater than 0xFFFF bytes
See Also:
`getExtra()`

#### getExtra

```
public byte[] getExtra()
```
Returns the extra field data for the entry.
Returns:
the extra field data for the entry, or null if none
See Also:
`setExtra(byte[])`

#### setComment

```
public void setComment(String comment)
```
Sets the optional comment string for the entry.ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.
Parameters:
`comment` - the comment string
See Also:
`getComment()`

#### getComment

```
public String getComment()
```
Returns the comment string for the entry.
Returns:
the comment string for the entry, or null if none
See Also:
`setComment(String)`

#### isDirectory

```
public boolean isDirectory()
```
Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.
Returns:
true if this is a directory entry

#### toString

```
public String toString()
```
Returns a string representation of the ZIP entry.
Overrides:
`toString` in class `Object`
Returns:
a string representation of the object.

#### hashCode

```
public int hashCode()
```
Returns the hash code value for this entry.
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
Returns a copy of this entry.
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

