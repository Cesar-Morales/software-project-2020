
function verMapa(centercoordinates){ 
    console.log(centercoordinates)
    var res = centercoordinates.split(',')
    var lat = res[0]
    var long = res[1]
    console.log(res)
    console.log(lat)
    console.log(long)
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

    var marker = L.marker([lat,long],{icon:myIcon})
    .addTo(myMap)
    myMap.setView([lat,long],13)
    console.log("PROBANDO");
    return false;
 
}