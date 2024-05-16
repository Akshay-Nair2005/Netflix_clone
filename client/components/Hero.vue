<template>
    <div
        class="container bg-[url('@/assets/img/kpp2.jpeg')] h-[600px] bg-cover w-[98.9vw] bg-no-repeat max-md:bg-black max-md:w-[100%] max-md:h-[100%]">

        <div class="w-full h-full bg-black bg-opacity-65">
            <Hcontent :star="img" :name="name" />
            <!-- <Corousal /> -->
        </div>
    </div>
</template>

<script>
import Hcontent from './Hcontent.vue';
import img from '@/assets/img/star.svg';

export default {
    data() {
        return {
            img,
            name: 'Akshay'
        };
    }
};



</script>

<style>
.container {
    overflow-x: hidden;
}
</style>