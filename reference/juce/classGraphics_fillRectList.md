#### fillRectList() [2/2]


 void Graphics::fillRectList ( const RectangleList< int > & rectangles ) const 
 

Fills a set of rectangles using the current colour or brush.If you have a lot of rectangles to draw, it may be more efficient to create a RectangleList and use this method than to call fillRect() multiple times.