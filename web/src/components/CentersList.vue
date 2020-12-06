<template>
    <div class="card Centers-List">
        <ul class="list-group list-group-flush">
            <li 
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
        centers: Array
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