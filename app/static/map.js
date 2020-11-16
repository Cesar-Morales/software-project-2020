
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


 $('table tr td').click(function(){
    var coordenadas = 
    var marker = L.marker([coordenadas],{icon:myIcon})
    .addTo(myMap)
    myMap.setView([coordenadas],13)
    console.log("PROBANDO");
    return false;
 });
