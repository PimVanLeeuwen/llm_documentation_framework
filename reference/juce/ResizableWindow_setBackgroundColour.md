#### setBackgroundColour()


 void ResizableWindow::setBackgroundColour ( Colour newColour ) 
 

Changes the colour currently being used for the window's background.As a convenience the window will fill itself with this colour, but you can override the paint() method if you need more customised behaviour.Note that the opaque state of this window is altered by this call to reflect the opacity of the colour passedin. On window systems which can't support semitransparent windows this might cause problems, (though it's unlikely you'll be using this class as a base for a semitransparent component anyway).You can also use the ResizableWindow::backgroundColourId colour id to set this colour.See alsogetBackgroundColour