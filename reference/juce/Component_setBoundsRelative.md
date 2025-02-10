#### setBoundsRelative() [2/2]


 void Component::setBoundsRelative ( Rectangle< float > proportionalArea ) 
 

Changes the component's position and size in terms of fractions of its parent's size.The values are factors of the parent's size, so for example setBoundsRelative ({ 0.2f, 0.2f, 0.5f, 0.5f }) would give it half the width and height of the parent, with its topleft position 20% of the way across and down the parent.See alsosetBounds