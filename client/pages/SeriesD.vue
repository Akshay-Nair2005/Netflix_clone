<template>
    <div class="text-white bg-black"><br><br>
        <h1 class="text-[36px] font-bold text-center font-serif text-red-600">{{ movie.name }}</h1>
        <div class="flex">
            <div class="flex">
                <iframe class="object-cover w-[800px] h-[500px] ml-8" :src="movie.trailer"></iframe>
            </div><br><br><br>
            <div class="block h-[100%]  w-[80%]">
                <div class="flex  justify-center item-center  w-[200px] h-[300px] ml-[27%] ">
                    <img :src="movie.image" alt="">
                </div>
                <div class=" flex justify-center w-[80%] gap-4 mt-8">
                    <img src="@/assets/img/star.svg" alt="movier" class="w-6 h-6 flex-col">
                    <h2 class="text-[15px] text-justify">{{ movie.rating }}</h2>
                </div><br>
                <h2 class="text-[15px] text-center flex items-center justify-center w-[80%]">Cast: {{ movie.cast }}</h2>
                <h2 class="text-[15px] text-center flex items-center justify-center w-[80%]">{{ movie.genre }}</h2>
                <p class="flex flex-col justify-center  text-center ml-8 mt-8 items-center w-[80%]">Description: {{
                    movie.description }}
                </p>
            </div>

        </div>
        <div v-for="season in movie.seasons" :key="season.id" class="mt-24 ml-8">
            <h1 class="text-[36px] text-center font-serif text-red-600">Season {{ season.number }}</h1>
            <p class="text-[21px]">Episode Count: {{ season.episode_count }}</p><br>
            <h4 class="text-[21px]">Episodes:</h4><br>
            <ul class="flex gap-5 ">
                <li v-for="episode in season.episodes" :key="episode.id"
                    class=" border-[#111] border-4 w-[15%] rounded-lg text-center hover:scale-105 leading-8 bg-[#111] ">
                    <img :src="movie.image" alt="img" class="w-[100%] h-52">
                    <h5 class="text-red-600 font-bold">{{ episode.name }}</h5>
                    <p>Episode Number: {{ episode.episode_number }}</p>
                    <p>Rating: {{ episode.rating }}</p>
                    <p>Duration: {{ episode.duration }}</p>
                    <p>Genre: {{ episode.genre }}</p><br>
                </li><br><br>
            </ul><br><br>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const movie = ref({});
const route = useRoute();
const movieId = ref(route.query.id)

function getTrailerUrl(trailer) {
    if (typeof trailer === 'string') {
        return trailer.replace(/\/\//g, '/');
    } else {
        return '';
    }
}

onMounted(async () => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/series/${movieId.value}`)
        if (!response.ok) {
            throw new Error(`Failed to fetch movie. Status: ${response.status}`);
        }
        const data = await response.json();
        movie.value = data;
        console.log('Movie trailer:', movie.value.trailer); // Debugging statement
    } catch (error) {
        console.error('Error fetching movie:', error);
    }
})
</script>

<style></style>