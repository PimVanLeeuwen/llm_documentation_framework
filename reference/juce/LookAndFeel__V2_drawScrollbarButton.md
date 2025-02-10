#### drawScrollbarButton()


 void LookAndFeel\_V2::drawScrollbarButton ( Graphics & g, ScrollBar & scrollbar, int width, int height, int buttonDirection, bool isScrollbarVertical, bool isMouseOverButton, bool isButtonDown ) overridevirtual 
 

Draws one of the buttons on a scrollbar.Parameters

 g the context to draw into 
 
 scrollbar the bar itself 
 width the width of the button 
 height the height of the button 
 buttonDirection the direction of the button, where 0 = up, 1 = right, 2 = down, 3 = left 
 isScrollbarVertical true if it's a vertical bar, false if horizontal 
 isMouseOverButton whether the mouse is currently over the button (also true if it's held down) 
 isButtonDown whether the mouse button's held down 


Implements ScrollBar::LookAndFeelMethods.