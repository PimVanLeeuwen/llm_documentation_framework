#### nextBytes

```
public void nextBytes(byte[] bytes)
```
Generates random bytes and places them into a user-supplied
byte array. The number of random bytes produced is equal to
the length of the byte array.The method `nextBytes` is implemented by class `Random`
as if by:
```
 
 public void nextBytes(byte[] bytes) {
   for (int i = 0; i < bytes.length; )
     for (int rnd = nextInt(), n = Math.min(bytes.length - i, 4);
          n-- > 0; rnd >>= 8)
       bytes[i++] = (byte)rnd;
 }
```

Parameters:
`bytes` - the byte array to fill with random bytes
Throws:
`NullPointerException` - if the byte array is null
Since:
1.1

