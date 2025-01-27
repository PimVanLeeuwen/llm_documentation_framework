#### toString

```
public String toString()
```
Returns a string representation of this bit set. For every index
for which this `BitSet` contains a bit in the set
state, the decimal representation of that index is included in
the result. Such indices are listed in order from lowest to
highest, separated by ", " (a comma and a space) and
surrounded by braces, resulting in the usual mathematical
notation for a set of integers.Example:
```

 BitSet drPepper = new BitSet();
```
Now `drPepper.toString()` returns "`{}`".
```

 drPepper.set(2);
```
Now `drPepper.toString()` returns "`{2}`".
```

 drPepper.set(4);
 drPepper.set(10);
```
Now `drPepper.toString()` returns "`{2, 4, 10}`".
Overrides:
`toString` in class `Object`
Returns:
a string representation of this bit set

