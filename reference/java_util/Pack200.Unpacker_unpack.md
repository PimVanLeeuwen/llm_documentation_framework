#### unpack

```
void unpack(File in,
            JarOutputStream out)
     throws IOException
```
Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.Does not close its output. (The output can accumulate more elements.)
Parameters:
`in` - a File.
`out` - a JarOutputStream.
Throws:
`IOException` - if an error is encountered.

