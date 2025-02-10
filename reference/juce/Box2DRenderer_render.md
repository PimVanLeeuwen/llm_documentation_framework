#### render()


 void Box2DRenderer::render ( Graphics & g, 
 
 b2World & world, 
 float box2DWorldLeft, 
 float box2DWorldTop, 
 float box2DWorldRight, 
 float box2DWorldBottom, 
 const Rectangle< float > & targetArea ) 

Renders the world.Parameters

 g the context to render into 
 
 world the world to render 
 box2DWorldLeft the left coordinate of the area of the world to be drawn 
 box2DWorldTop the top coordinate of the area of the world to be drawn 
 box2DWorldRight the right coordinate of the area of the world to be drawn 
 box2DWorldBottom the bottom coordinate of the area of the world to be drawn 
 targetArea the area within the target context onto which the source world rectangle should be mapped