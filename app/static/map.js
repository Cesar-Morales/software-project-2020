

const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

let myMap = L.map('mapid').setView([-34.6083,-58.3712],13)

L.tileLayer(tilesProvider,{
    maxZoom:18,
}).addTo(myMap)

var myIcon = L.icon({
    iconUrl:"../static/marker.png",
    iconSize:[50,32],
    iconAnchor:[25,16],
})

  
    myMap.setView([-34.6083,-58.3712],13)
    console.log("PROBANDO");
    
    var popup = L.popup();

    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("Coordenadas seleccionadas" + e.latlng.toString())
            .openOn(myMap);
        var lat = e.latlng.lat;
        var lng = e.latlng.lng;    
        console.log(lat,lng);
     document.getElementById('coordinates').value=lat.toString()+','+lng.toString()       
    }
    
    myMap.on('click', onMapClick);
    
    
function verMapa(centercoordinates){ 
    console.log(centercoordinates)
    var res = centercoordinates.split(',')
    var lat = res[0]
    var long = res[1]
    console.log(res)
    console.log(lat)
    console.log(long)
    marker = L.marker([lat,long]).addTo(myMap)
    myMap.setView([lat,long],10)

    }

    // return false;
 
// }