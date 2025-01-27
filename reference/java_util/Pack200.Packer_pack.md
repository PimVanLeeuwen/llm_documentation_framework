#### pack

```
void pack(JarInputStream in,
          OutputStream out)
   throws IOException
```
Takes a JarInputStream and converts it into a Pack200 archive.Closes its input but not its output. (Pack200 archives are appendable.)The modification time and deflation hint attributes are not available,
for the JAR manifest file and its containing directory.
Parameters:
`in` - a JarInputStream
`out` - an OutputStream
Throws:
`IOException` - if an error is encountered.
See Also:
`MODIFICATION_TIME`,
`DEFLATE_HINT`

