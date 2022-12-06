# Wardrobify

Team:
* Steven Duong - Hats
* Jamal Degeratto - Shoes

## How to run application

Open up terminal.
CD into projects (or a folder of your choice).
clone file from GitLab: git clone https://gitlab.com/Jamal-Jamal/microservice-two-shot
CD into the clone (microservice-two-shot).

Open up docker desktop to start to build and compose containers.
Commands to run to bring up containers:
docker volume create pgdata
docker-compose build
docker-compose up

Open up VScode in terminal with command "code ."

After these commands are ran, open up insomnia.
Create a location folder for hats.
In that folder create a post request to create the location.
The URL is "http://localhost:8100/api/locations/"
In the JSON body, have the following object:
{
	"closet_name": "small closet",
	"section_number": "2",
	"shelf_number": "2"
}
Hit send to create a location for the hats.

Create a get request to show location.
The URL is "http://localhost:8100/api/locations"

Create a Hats folder.
In that folder create a post request to create a hat.
The URL is "http://localhost:8090/api/hats/"
In the JSON body, have the following object:
{
    "fabric": "soft",
    "style": "bucket",
    "color": "blue",
    "picture_url": null,
	"location": 1
}
Note ***(You can choose your own values, the above is just an example. If you do not have a picture URL, you can input null for now)***
Hit send to create a hat.

***Sample Response data for post request***
{
	"fabric": "soft",
	"style": "bucket",
	"color": "blue",
	"picture_url": null,
	"location": {
		"closet_name": "nice",
		"section_number": 1,
		"shelf_number": 1,
		"import_href": "/api/locations/1/"
	},
	"id": 1
}

To show a specific hat, create a get request to "http://localhost:8090/api/hats/1/" (or whatever id is connected to your hat)
To get a list of hats, create a get request to "http://localhost:8090/api/hats/"
To delete a hat, create a delete request to "http://localhost:8090/api/hats/1/" (or whatever id is connected to your hat)


Now do the same for shoes...
Create a bin folder for shoes.

In that folder create a POST request to create the bin.
The URL is "http://localhost:8100/api/bins/"
In the JSON body, have the following object:
{
	"closet_name": " ",
	"bin_number": 1,
	"bin_size": 3
}
Hit send to create a bin for the shoes.

Create a GET request to show bin.
The URL is "http://localhost:8100/api/bins/"

Create a Shoes folder.
In that folder create a POST request to create a Shoe.
The URL is "http://localhost:8080/api/shoes/"
In the JSON body, have the following object:
{
    "model_name": " ",
    "manufacturer": " ",
    "color": " ",
    "picture_url": null,
	"bin": 1
}


Hit send to create a shoe.

To show a specific shoe, create a GET request to "http://localhost:8080/api/shoes/1/" (or whatever id is connected to your shoe)
To get a list of shoes, create a GET request to "http://localhost:8080/api/shoes/"
To delete a hat, create a DELETE request to "http://localhost:8080/api/shoes/1/" (or whatever id is connected to your shoe)


Open your browser to localhost:3000 and start creating shoes and hats for your wardrobe!

Identify Value objects for Hats:
closet_name
shelf_number
section_number
import_href

Identify Value objects for Shoes:
closet_name
bin_number
bin_size
import_href

URLS and PORTS
Use the following urls for Insomnia. Each request should have these respective endpoints in insomnia.

RESTful API endpoints: HATS
UPDATE HAT- PUT REQUEST = http://localhost:8090/api/hats/int:pk/
DELETE HAT- DELETE REQUEST = http://localhost:8090/api/hats/int:pk/
DETAIL HAT- GET REQUEST = http://localhost:8090/api/hats/int:pk/
LIST HATS- GET REQUEST = http://localhost:8090/api/hats/
CREATE HAT- POST REQUEST = http://localhost:8090/api/hats/

RESTful API endpoints: Shoes
UPDATE HAT- PUT REQUEST = http://localhost:8080/api/shoes/int:pk/
DELETE HAT- DELETE REQUEST = http://localhost:8080/api/shoes/int:pk/
DETAIL HAT- GET REQUEST = http://localhost:8080/api/shoes/int:pk/
LIST HATS- GET REQUEST = http://localhost:8080/api/shoes/
CREATE HAT- POST REQUEST = http://localhost:8080/api/shoes/

Urls for Locations in Wardrobe API
LIST LOCATIONS- GET REQUEST = http://localhost:8100/api/locations/
LOCATION DETAIL- GET REQUEST = http://localhost:8100/api/locations/int:pk/
UPDATE LOCATION- PUT REQUEST = http://localhost:8100/api/locations/int:pk/
DELETE LOCATION- DELETE REQUEST = http://localhost:8100/api/locations/int:pk/
CREATE LOCATION- POST REQUEST = http://localhost:8100/api/locations/

Urls for Bins in Wardrobe API
LIST LOCATIONS- GET REQUEST = http://localhost:8100/api/bins/
LOCATION DETAIL- GET REQUEST = http://localhost:8100/api/bins/int:pk/
UPDATE LOCATION- PUT REQUEST = http://localhost:8100/api/bins/int:pk/
DELETE LOCATION- DELETE REQUEST = http://localhost:8100/api/bins/int:pk/
CREATE LOCATION- POST REQUEST = http://localhost:8100/api/bins/


Ports
shoes api-1 = 8080:8000
hats api-1 = 8090:8000


## Design

https://gitlab.com/Jamal-Jamal/microservice-two-shot/-/blob/main/Microservice-two-shotDDD.png 

## Shoes microservice

The shoes microservice will pull from the Wardrobify API. It will contain a list of shoes that will include manufacturer, model_name, color, picture URL, and a bind in the shoe wardrobe where it exists. The value objects in the bin that is polled from the Wardrobe API has these attributes:  closet_name, bin_number, bin_size, and import href.


## Hats microservice

The hats microservice will pull from the Wardrobify API. It will contain a list of hats that will include fabric, style, color, picture URL, and a location in the hat wardrobe where it exists. The value objects in the location that is polled from the Wardrobe API has these attributes:  shelf number, closet name, section number, and import href.
