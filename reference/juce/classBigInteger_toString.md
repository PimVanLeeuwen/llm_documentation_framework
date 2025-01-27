#### toString()


 String BigInteger::toString ( int base, 
 
 int minimumNumCharacters = 1 ) const 

Converts the number to a string.Specify a base such as 2 (binary), 8 (octal), 10 (decimal), 16 (hex). If minimumNumCharacters is greater than 0, the returned string will be padded with leading zeros to reach at least that length.