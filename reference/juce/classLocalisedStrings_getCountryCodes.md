#### getCountryCodes()


 const StringArray & LocalisedStrings::getCountryCodes ( ) const 
 

Returns the list of suitable country codes listed in the translation file.These is specified in the file using a line starting with "countries:", e.g.countries: fr be mc ch lu
The country codes are supposed to be 2character ISO compliant codes.