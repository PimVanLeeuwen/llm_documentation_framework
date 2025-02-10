#### setImages()


 void DrawableButton::setImages ( const Drawable \* normalImage, 
 
 const Drawable \* overImage = nullptr, 
 const Drawable \* downImage = nullptr, 
 const Drawable \* disabledImage = nullptr, 
 const Drawable \* normalImageOn = nullptr, 
 const Drawable \* overImageOn = nullptr, 
 const Drawable \* downImageOn = nullptr, 
 const Drawable \* disabledImageOn = nullptr ) 

Sets up the images to draw for the various button states.The button will keep its own internal copies of these drawables.Parameters

 normalImage the thing to draw for the button's 'normal' state. An internal copy will be made of the object passedin if it is nonnull. 
 
 overImage the thing to draw for the button's 'over' state if this is null, the button's normal image will be used when the mouse is over it. An internal copy will be made of the object passedin if it is nonnull. 
 downImage the thing to draw for the button's 'down' state if this is null, the 'over' image will be used instead (or the normal image as a last resort). An internal copy will be made of the object passedin if it is nonnull. 
 disabledImage an image to draw when the button is disabled. If this is null, the normal image will be drawn with a reduced opacity instead. An internal copy will be made of the object passedin if it is nonnull. 
 normalImageOn same as the normalImage, but this is used when the button's toggle state is 'on'. If this is nullptr, the normal image is used instead 
 overImageOn same as the overImage, but this is used when the button's toggle state is 'on'. If this is nullptr, the normalImageOn is drawn instead 
 downImageOn same as the downImage, but this is used when the button's toggle state is 'on'. If this is nullptr, the overImageOn is drawn instead 
 disabledImageOn same as the disabledImage, but this is used when the button's toggle state is 'on'. If this is nullptr, the normal image will be drawn instead with a reduced opacity