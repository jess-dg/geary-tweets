function initialize() {
                    var mapOptions = {
                    center: new google.maps.LatLng(60.439698,113.818359),
                    zoom: 8,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                    };

                    var marker = new google.maps.Marker({
                    position: myLatlng,
                    title:tweet.tweet_text
                    });

                    var map = new google.maps.Map(document.getElementById("map-canvas"),
                        mapOptions);

                    var myLatlng = new google.maps.LatLng(tweet.lattitude,tweet.longitude);


            }

      google.maps.event.addDomListener(window, 'load', initialize);

      marker.setMap(map);