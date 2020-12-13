
const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

const myMap = L.map('mapid').setView([-34.6083,-58.3712],13)

L.tileLayer(tilesProvider,{
    maxZoom:18,
}).addTo(myMap)
myMap.setView([-34.6083,-58.3712],13)


function verMapa(centercoordinates){ 
    console.log(centercoordinates)
    var res = centercoordinates.split(',')
    var lat = res[0]
    var long = res[1]
    console.log(res)
    console.log(lat)
    console.log(long)
    marker = L.marker([lat.toString(),long.toString()]).addTo(myMap)
    myMap.setView([lat,long],10)
   

    }