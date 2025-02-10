#### drawBevel()


 static void LookAndFeel\_V2::drawBevel ( Graphics & , int x, int y, int width, int height, int bevelThickness, const Colour & topLeftColour = Colours::white, const Colour & bottomRightColour = Colours::black, bool useGradient = true, bool sharpEdgeOnOutside = true ) static 
 

Draws a 3D raised (or indented) bevel using two colours.The bevel is drawn inside the given rectangle, and greater bevel thicknesses extend inwards.The topleft colour is used for the top and lefthand edges of the bevel; the bottomright colour is used for the bottom and righthand edges.If useGradient is true, then the bevel fades out to make it look more curved and less angular. If sharpEdgeOnOutside is true, the outside of the bevel is sharp, and it fades towards the centre; if sharpEdgeOnOutside is false, then the centre edges are sharp and it fades towards the outside.