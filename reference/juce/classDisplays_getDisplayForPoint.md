#### getDisplayForPoint()


 const Display \* Displays::getDisplayForPoint ( Point< int > point, bool isPhysical = false ) const noexcept 
 

Returns the Display object representing the display containing a given Point (either in logical or physical pixels), or nullptr if there are no connected displays.If the Point lies outside all the displays then the nearest one will be returned.