##City Pollutant CRUD operation##

#Create a class city_data with following class methods.#

a.	add_pollutant_details(self) : should ask user to enter pollutant value of co,no2,co2 and city name and store it in below mentioned format:

`{`
`“ts” : 1660807659`
`“city_name:” “pune”,`
`“co” : 45,`	
`“no2” : 47,`
`“co2” : 87`
`}`

Note If city name already exists, it should ask user to enter a new city name then only store the new pollutant records, if user again enters the same, display “aborting” and exit.

b.	display_pollutant_details(self) : should display all the values entered by the user : The format is mentioned below:

`[`
`{`
` 	“ts” : 1660807659`
`“city_name:” “pune”,`
`“co” : 45,	`
`“no2” : 47,`
`“co2” : 87`
`},`
`{`
` 	“ts” : 1660807662`
`“city_name:” “chennai”,`
`“co” : 45,	`
`“no2” : 47,`
`“co2” : 87`
`}`
`]`

c.	update_pollutant_details(self): if the city name exists then user should be able to update the value for example “city_name” pune with updated pollutant details should look like this:

`{`
` 	“ts” : 1660807659`
`“city_name:” “pune”,`
`“co” :   55,`	
`“no2” : 57,`
`“co2” : 67`
`}`

d.	delete_pollutant_detail(self):ask user to enter the ts value, if ts value exist then delete the entry of the pollutant.
Data in the records before delete operation:

`[`
`{`
` 	“ts” : 1660807659`
`“city_name:” “pune”,`
`“co” : 45,`	
`“no2” : 47,`
`“co2” : 87`
`},`
`{`
` 	“ts” : 1660807662`
`“city_name:” “chennai”,`
`“co” : 45,	`
`“no2” : 47,`
`“co2” : 87`
`}`
`]`

User enters the ts = 1660807662
Data after the delete operation:

`[`
`{`
` 	“ts” : 1660807659`
`“city_name:” “pune”,`
`“co” : 45,`	
`“no2” : 47,`
`“co2” : 87`
`}`
`]`

Note: The user should be able to select from the menu which operation he is interested to perform for example, 
if a user enters value 1: then call add_pollutant_details() method and user should be able to add pollutant details.
If user enters value 2, then call display_pollutant_details() method and display the existing details and
if user enters value 3, it should call update_pollutant_details() method and user should be able to update the details 
if 4 then it should call the delete_pollutant_detail method and able to delete the entry if exists.
