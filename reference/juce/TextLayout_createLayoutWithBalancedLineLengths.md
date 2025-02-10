#### createLayoutWithBalancedLineLengths() [2/2]


 void TextLayout::createLayoutWithBalancedLineLengths ( const AttributedString & , 
 
 float maxWidth, 
 float maxHeight ) 

Creates a layout, attempting to choose a width which results in lines of a similar length.This will be slower than the normal createLayout method, but produces a tidier result.