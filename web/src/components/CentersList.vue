<template>
    <div class="card brew-list">
        <ul class="list-group list-group-flush">
            <li 
            v-bind:key="index"
            v-for="(centers,index) in centers"
            class="list-group-item"
            > {{center.name}}
            </li>
        </ul>
    </div>        
</template>
<script>
export default {
    name: 'CentersList',
    props: {
        centers:Array
    }
}
</script>
<style >
    .Centers-List{
        overflow-y:scroll;
        height: 95vh;

    }

</style>