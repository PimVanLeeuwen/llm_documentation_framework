#### getParameterNames()


 const StringArray & URL::getParameterNames ( ) const noexcept 
 

Returns an array of the names of all the URL's parameters.e.g. for the url "www.fish.com?type=haddock&amount=some+fish", this array would contain two items: "type" and "amount".You can call getParameterValues() to get the corresponding value of each parameter. Note that the list can contain multiple parameters with the same name.See alsogetParameterValues, withParameter