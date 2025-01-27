#### store

```
public void store(OutputStream out,
                  String comments)
           throws IOException
```
Writes this property list (key and element pairs) in this
`Properties` table to the output stream in a format suitable
for loading into a `Properties` table using the
`load(InputStream)` method.Properties from the defaults table of this `Properties`
table (if any) are not written out by this method.This method outputs the comments, properties keys and values in
the same format as specified in
`store(Writer)`,
with the following differences:The stream is written using the ISO 8859-1 character encoding.Characters not in Latin-1 in the comments are written as
`\u`xxxx for their appropriate unicode
hexadecimal value xxxx.Characters less than `\u0020` and characters greater
than `\u007E` in property keys or values are written
as `\u`xxxx for the appropriate hexadecimal
value xxxx.After the entries have been written, the output stream is flushed.
The output stream remains open after this method returns.
Parameters:
`out` - an output stream.
`comments` - a description of the property list.
Throws:
`IOException` - if writing this property list to the specified
output stream throws an IOException.
`ClassCastException` - if this `Properties` object
contains any keys or values that are not `Strings`.
`NullPointerException` - if `out` is null.
Since:
1.2

