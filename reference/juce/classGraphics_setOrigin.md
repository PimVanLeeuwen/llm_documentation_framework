#### setOrigin() [2/2]


 void Graphics::setOrigin ( int newOriginX, 
 
 int newOriginY ) 

Moves the position of the context's origin.This changes the position that the context considers to be (0, 0) to the specified position.So if you call setOrigin (100, 100), then the position that was previously referred to as (100, 100) will subsequently be considered to be (0, 0).See alsoreduceClipRegion, addTransform