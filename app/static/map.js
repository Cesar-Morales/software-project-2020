const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

let myMap = L.map('mapid').setView([51.505,-0.09],13)

L.tileLayer(tilesProvider,{
    maxZoom:18,
}).addTo(myMap)