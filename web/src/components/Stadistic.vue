<template>
    <div>
        <Pie></Pie>
        <Histogram></Histogram>
        <div class="heatmap">
            <Heatmap></Heatmap>
        </div>
        <Map></Map>
    </div>
</template>

<script>
import Pie from '../Stadistics/Pie'
import Histogram from '../Stadistics/Histogram'
import Heatmap from '../Stadistics/Heatmap'
import Map from '../Stadistics/Map'

export default {
    name: 'Stadistic',
    components: {
        Pie,
        Histogram,
        Heatmap,
        Map
  }
}
</script>

<style lang="scss" scoped>
</style>