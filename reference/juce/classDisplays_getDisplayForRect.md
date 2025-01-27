#### getDisplayForRect()


 const Display \* Displays::getDisplayForRect ( Rectangle< int > rect, bool isPhysical = false ) const noexcept 
 

Returns the Display object representing the display containing a given Rectangle (either in logical or physical pixels), or nullptr if there are no connected displays.If the Rectangle lies outside all the displays then the nearest one will be returned.