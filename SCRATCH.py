
Google maps API Key: AIzaSyAp4tN-lSHwX_6TIDME0Ev5JciDKlenxy0

#Throw data in a sqlite database or mongodb db
#Only created_at,
#id,
#id_string
#geo, (type, coordinates) What other type of "types" exist?
#coordinates
#Query the database for all tweets with lat/long in specific range
#Print tweets in longitude order on an html page.

#use google earth to get the geary st. elevation... sorta.

#Put all the database level stuff in a separate file (model def, sessions)
#Display.py -- flask app to query the tweets + use template.

geary_lat = 37.785063

contained_within place_id... "5a110d312052166f"
attribute:street_address "Geary%%20St"

GEARY PART I
"bounding_box": {
    "coordinates": [
      [
        [
          -122.402977,
            37.788235
        ],
        [
          -122.402077,
          37.788452
        ],
        [
          -122.404053,
            37.787285
        ],
        [
          -122.447395,
            37.781605
        ],
        [
          -122.447784,
            37.783840
        ]
      ]
    ],
    "type": "Polygon"
  },
  "id": "247f43d441defc03",
  "contained_within": [
    {
      "name": "San Francisco",
      "country": "United States",
      "country_code": "US",
      "attributes": {
 
      },


GEARY PART II


"bounding_box": {
    "coordinates": [
      [
        [
          -122.447739,
            37.783707
        ],
        [
          -122.509583,
            37.779499
        ],
        [
          -122.509407,
            37.777771
        ],
        [
          -122.447311,
            37.781536
        ],
        [
          -122.402977,
            37.788235
        ]
      ]
    ],
    "type": "Polygon"
  },
  "id": "247f43d441defc03",
  "contained_within": [
    {
      "name": "San Francisco",
      "country": "United States",
      "country_code": "US",
      "attributes": {
 
      },

      http://stream.twitter.com/1/statuses/filter.json\?locations\=-122.447739,37.783707,-122.447311,37.781536,-122.509407,37.777771,-122.509583,37.779499,-122.447739,37.783707
"http://api.twitter.com/1/geo/id/247f43d441defc03.json"


