#### setSeed

```
public void setSeed(long seed)
```
Sets the seed of this random number generator using a single
`long` seed. The general contract of `setSeed` is
that it alters the state of this random number generator object
so as to be in exactly the same state as if it had just been
created with the argument `seed` as a seed. The method
`setSeed` is implemented by class `Random` by
atomically updating the seed to
```
 (seed ^ 0x5DEECE66DL) & ((1L << 48) - 1)
```
and clearing the `haveNextNextGaussian` flag used by `nextGaussian()`.The implementation of `setSeed` by class `Random`
happens to use only 48 bits of the given seed. In general, however,
an overriding method may use all 64 bits of the `long`
argument as a seed value.
Parameters:
`seed` - the initial seed

