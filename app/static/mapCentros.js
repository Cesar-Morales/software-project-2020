
const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
let myMap = L.map('mapid').setView([-34.6083,-58.3712],13)
let marker = L.marker()
L.tileLayer(tilesProvider,{
    maxZoom:18,
}).addTo(myMap)


var popup = L.popup();

function abrirPopUp(lat,lng,centername){
    copia = {'lat':lat,'lng':lng}
    popup
        .setLatLng(copia)
        .setContent("Nombre de Centro:"+centername)
        .openOn(myMap)
}


function verMapa(centercoordinates,centername){ 
    console.log(centercoordinates)
    var res = centercoordinates.split(',')
    var lat = res[0]
    var long = res[1]
    console.log(res)
    console.log(lat)
    console.log(long)
    console.log(centername)
    marker = L.marker([lat.toString(),long.toString()]).addTo(myMap)
    marker.on('click',abrirPopUp(lat,long,centername));
    myMap.setView([lat,long],10)
   

    }