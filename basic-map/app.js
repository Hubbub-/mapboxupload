L.mapbox.accessToken = 'pk.eyJ1IjoiYnJhZWRlbmYiLCJhIjoiY2lvZGs1MHk5MDA4N3YxbTN4cTBpbmVyYSJ9.g1-OkxRnSdG8pqtEhCjPaA';
  var map = L.mapbox.map('map', 'mapbox.streets')
  .setView([41.234024, -73.799021], 9);

  var myLayer = L.mapbox.featureLayer().addTo(map);
    
  var featureLayer = L.mapbox.featureLayer()
    .loadURL('vlog.geojson')
    .addTo(map);
    
    featureLayer.on('mouseover', function(e) {
        e.layer.openPopup();
    });
    featureLayer.on('mouseout', function(e) {
        e.layer.closePopup();
    });