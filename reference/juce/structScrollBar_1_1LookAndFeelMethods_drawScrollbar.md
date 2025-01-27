#### drawScrollbar()


 virtual void ScrollBar::LookAndFeelMethods::drawScrollbar ( Graphics & g, ScrollBar & scrollbar, int x, int y, int width, int height, bool isScrollbarVertical, int thumbStartPosition, int thumbSize, bool isMouseOver, bool isMouseDown ) pure virtual 
 

Draws the thumb area of a scrollbar.Parameters

 g the context to draw into 
 
 scrollbar the bar itself 
 x the x position of the left edge of the thumb area to draw in 
 y the y position of the top edge of the thumb area to draw in 
 width the width of the thumb area to draw in 
 height the height of the thumb area to draw in 
 isScrollbarVertical true if it's a vertical bar, false if horizontal 
 thumbStartPosition for vertical bars, the y coordinate of the top of the thumb, or its x position for horizontal bars 
 thumbSize for vertical bars, the height of the thumb, or its width for horizontal bars. This may be 0 if the thumb shouldn't be drawn. 
 isMouseOver whether the mouse is over the thumb area, also true if the mouse is currently dragging the thumb 
 isMouseDown whether the mouse is currently dragging the scrollbar 


Implemented in LookAndFeel\_V1, LookAndFeel\_V2, LookAndFeel\_V3, and LookAndFeel\_V4.