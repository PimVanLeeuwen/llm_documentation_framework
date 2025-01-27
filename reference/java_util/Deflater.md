```
public class Deflater
extends Object
```
This class provides support for general purpose compression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the java.util.zip
package description.The following code fragment demonstrates a trivial compression
and decompression of a string using Deflater and
Inflater.
```

 try {
     // Encode a String into bytes
     String inputString = "blahblahblah";
     byte[] input = inputString.getBytes("UTF-8");

     // Compress the bytes
     byte[] output = new byte[100];
     Deflater compresser = new Deflater();
     compresser.setInput(input);
     compresser.finish();
     int compressedDataLength = compresser.deflate(output);
     compresser.end();

     // Decompress the bytes
     Inflater decompresser = new Inflater();
     decompresser.setInput(output, 0, compressedDataLength);
     byte[] result = new byte[100];
     int resultLength = decompresser.inflate(result);
     decompresser.end();

     // Decode the bytes into a String
     String outputString = new String(result, 0, resultLength, "UTF-8");
 } catch(java.io.UnsupportedEncodingException ex) {
     // handle
 } catch (java.util.zip.DataFormatException ex) {
     // handle
 }
 
```

See Also:
`Inflater`
