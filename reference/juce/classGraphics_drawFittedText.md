#### drawFittedText() [2/2]


 void Graphics::drawFittedText ( const String & text, 
 
 Rectangle< int > area, 
 Justification justificationFlags, 
 int maximumNumberOfLines, 
 float minimumHorizontalScale = 0.0f ) const 

Tries to draw a text string inside a given space.This does its best to make the given text readable within the specified rectangle, so it's useful for labelling things.If the text is too big, it'll be squashed horizontally or broken over multiple lines if the maximumLinesToUse value allows this. If the text just won't fit into the space, it'll cram as much as possible in there, and put some ellipsis at the end to show that it's been truncated.A Justification parameter lets you specify how the text is laid out within the rectangle, both horizontally and vertically.The minimumHorizontalScale parameter specifies how much the text can be squashed horizontally to try to squeeze it into the space. If you don't want any horizontal scaling to occur, you can set this value to 1.0f. Pass 0 if you want it to use a default value.See alsoGlyphArrangement::addFittedText