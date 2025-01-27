#### hashCode

```
public int hashCode()
```
Returns the hash code value for this bit set. The hash code depends
only on which bits are set within this `BitSet`.The hash code is defined to be the result of the following
calculation:
```
 
 public int hashCode() {
     long h = 1234;
     long[] words = toLongArray();
     for (int i = words.length; --i >= 0; )
         h ^= words[i] * (i + 1);
     return (int)((h >> 32) ^ h);
 }
```
Note that the hash code changes if the set of bits is altered.
Overrides:
`hashCode` in class `Object`
Returns:
the hash code value for this bit set
See Also:
`Object.equals(java.lang.Object)`,
`System.identityHashCode(java.lang.Object)`

