<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map_canvas { height: 100% }
    </style>
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCtnTt4diLgTb8nC0P9FCFttB2GgdHLGqk&sensor=true">
    </script>
    <script type="text/javascript">
     var map;
     var geocoder;
     var marker = null;
     function initialize() {
       geocoder = new google.maps.Geocoder();
       var myLatlng = new google.maps.LatLng(0,0);
       var mapOptions = {
       zoom: 1,
       center: myLatlng,
       mapTypeId: google.maps.MapTypeId.ROADMAP
      }
     map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

     google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
        }); 
     }
  
       //;;  document.getElementById("pp").innerHTML="anything";
     
    function placeMarker(location) {
     if(marker)
      {
        marker.setMap(null);   
      }
     marker = new google.maps.Marker({
      position: location,
      map: map
       });
     
            
     if(marker)
      {
       document.getElementById("p").innerHTML = location;
      }
      // geo coding function 

      var ll = marker.getPosition();
      geocoder.geocode({'latLng': ll}, function(results, status) {
         if (status == google.maps.GeocoderStatus.OK) {
             if (results[1]) {
             map.setZoom(1);
             document.getElementById("pp").innerHTML=results[1].formatted_address;
             }
         }
        else {
            document.getElementById("pp").innerHTML ="not a country";
           marker.setMap(null);
         }
     });

  }
    </script>
  </head>
  <body onload="initialize()">
    <div id="map_canvas" style="width:50%; height:50%"></div>
    <p id="pp"></p>
    <p id="p"></p>
  </body>
</html>

