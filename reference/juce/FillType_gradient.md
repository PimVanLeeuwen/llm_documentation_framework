#### gradient


 std::unique\_ptr<ColourGradient> FillType::gradient 
 

Returns the gradient that should be used for filling.This will be nullptr if the object is some other type of fill. If a gradient is active, the overall opacity with which it should be applied is indicated by the alpha channel of the colour variable.