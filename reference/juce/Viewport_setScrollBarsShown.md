#### setScrollBarsShown()


 void Viewport::setScrollBarsShown ( bool showVerticalScrollbarIfNeeded, 
 
 bool showHorizontalScrollbarIfNeeded, 
 bool allowVerticalScrollingWithoutScrollbar = false, 
 bool allowHorizontalScrollingWithoutScrollbar = false ) 

Turns scrollbars on or off.If set to false, the scrollbars won't ever appear. When true (the default) they will appear only when needed.The allowVerticalScrollingWithoutScrollbar parameters allow you to enable mousewheel scrolling even when there the scrollbars are hidden. When the scrollbars are visible, these parameters are ignored.