#### getMaxValue()


 double Slider::getMaxValue ( ) const 
 

For a slider with two or three thumbs, this returns the higher of its values.For a twovalue slider, the values are controlled with getMinValue() and getMaxValue(). A slider with three values also uses the normal getValue() and setValue() methods to control the middle value.See alsogetMinValue, TwoValueHorizontal, TwoValueVertical, ThreeValueHorizontal, ThreeValueVertical