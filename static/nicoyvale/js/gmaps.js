
  function initMap() {
      var recepcion_coord = {lat: -0.105258, lng: -78.503670};
      var ceremonia_coord = {lat: -0.103265, lng: -78.500863};

      var mapOtions = {
        zoom: 16,
        minZoom: 13,
        maxZoom: 17,
        center: ceremonia_coord,

      }

      var mapCanvas = document.getElementById('map');

      var map = new google.maps.Map(mapCanvas, mapOtions);

      var recepcion_marker = new google.maps.Marker({
        position: recepcion_coord,
        map: map
      });

      var ceremonia_marker = new google.maps.Marker({
        position: ceremonia_coord,
        map: map
      });

      var recepcion_string = '<div class="info-window">' +
                '<div class="info-content">' +
                '<h5>Villa Vieja</h5>' +
                '<p>José Miguel Carrión<br> y Juan Procel</p>' +
                '<p><a href="https://waze.com/ul?ll='+recepcion_coord.lat+','+recepcion_coord.lng+'" target="blank" class="btn btn-primary">Abrir en Waze</a></p>'+
                '</div>' +
                '</div>';

      var recepcion_window = new google.maps.InfoWindow({
            content: recepcion_string,
            maxWidth: 200
      });

      recepcion_window.open(map, recepcion_marker);

      recepcion_marker.addListener('click', function () {
            recepcion_window.open(map, recepcion_marker);
      });

      var ceremonia_string = '<div class="info-window">' +
                '<div class="info-content">' +
                '<h5>Sagrada Familia</h5>' +
                '<p>José Gonzalo Cordero<br> y Descalzi</p>'+
                '<p><a href="https://waze.com/ul?ll='+ceremonia_coord.lat+','+ceremonia_coord.lng+'" target="blank" class="btn btn-primary">Abrir en Waze</a></p>'+
                '</div>' +
                '</div>';

      var ceremonia_window = new google.maps.InfoWindow({
            content: ceremonia_string,
            maxWidth: 200
      });

      ceremonia_window.open(map, ceremonia_marker);

      ceremonia_marker.addListener('click', function () {
            ceremonia_window.open(map, ceremonia_marker);
      });
    }

    google.maps.event.addDomListener(window, 'load', initMap);
