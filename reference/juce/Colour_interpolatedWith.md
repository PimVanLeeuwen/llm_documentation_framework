#### interpolatedWith()


 Colour Colour::interpolatedWith ( Colour other, float proportionOfOther ) const noexcept 
 

Returns a colour that lies somewhere between this one and another.If amountOfOther is zero, the result is 100% this colour, if amountOfOther is 1.0, the result is 100% of the other colour.