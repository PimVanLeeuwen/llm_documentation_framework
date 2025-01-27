#### createSpring()


 static std::function< float(float)> Easings::createSpring ( const SpringEasingOptions & options = {} ) static 
 

Returns an easing function that behaves like a spring with a weight attached.Like createEaseOutBack() this might overshoot causing it to return float values exceeding 1.0f.See alsocreateEaseOutBack