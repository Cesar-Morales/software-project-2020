<template>
    <div class="card Centers-List">
        <ul class="list-group list-group-flush">
            <li v-on:click='actualizar(index)'
            v-bind:key="index"
            v-for="(center,index) in centers"
            class="list-group-item"
            > {{center.name}}
            </li>
        </ul>
    </div>        
</template>
<script>

export default {
    name: 'CenterList',
    props: {
        onUpdate:Function,
        centers: Array,        
    },
    methods:
    {
        actualizar(index){
            var splitted = this.centers[index].coordinates.split(",");
            var lat = splitted[0];
            var lng = splitted[1];
            this.onUpdate(lat,lng);
        }
    }
    
}
</script>
<style lang="scss" scoped>
    .Centers-List{
        overflow-y:scroll;
        height: 95vh;
        li {
            &:hover{
                background-color: darkgray;
            }
        }

    }

</style>