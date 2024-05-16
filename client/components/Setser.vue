<template>
    <div><br>
        <select v-model="selectedGenre" @change="fetchSeriesByGenre" class="bg-black text-white">
            <option value="" class="bg-black text-white">All Genres</option>
            <option v-for="genre in genres" :value="genre" class="bg-black text-white">{{ genre }}</option>
        </select>

        <div v-if="selectedGenre === ''">
            <div class="flex gap-12">
                <div v-for="item in movies" :key="item.id" class="text-white">
                    <div
                        class="border-[#111] rounded-md  mt-8 border-4 h-[500px] w-[300px] shadow-xl bg-[#111] hover:scale-105">
                        <div>
                            <img :src="item.image" alt="" class="w-full h-[300px] object-cover">
                        </div><br>
                        <div>
                            <h1 class="text-[25px] text-center">{{ item.name }}</h1>
                        </div>
                        <div>
                            <h2 class="text-[15px] text-center">{{ item.rating }}</h2>
                        </div>
                        <div>
                            <h2 class="text-[15px] text-center">{{ item.genre }}</h2>
                        </div><br>
                        <div class="flex flex-col justify-center ml-8 w-[80%]">
                            <router-link :to="`./SeriesD?id=${item.id}`"
                                class="bg-red-600 hover:bg-red-700 p-3 rounded-lg text-center">
                                View More
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div v-else>
            <div class="flex gap-8">
                <div v-for="item in filteredMovies" :key="item.id" class="text-white">
                    <div
                        class="border-[#111] rounded-md mt-8 border-4 h-[500px] w-[300px] shadow-xl bg-[#111] hover:scale-105">
                        <div>
                            <img :src="item.image" alt="" class="w-full h-[300px] object-cover">
                        </div><br>
                        <div>
                            <h1 class="text-[25px] text-center">{{ item.name }}</h1>
                        </div>
                        <div>
                            <h2 class="text-[15px] text-center">{{ item.rating }}</h2>
                        </div>
                        <div>
                            <h2 class="text-[15px] text-center">{{ item.genre }}</h2>
                        </div><br>
                        <div class="flex flex-col justify-center ml-8 w-[80%]">
                            <router-link :to="`./Description?id=${item.id}`"
                                class="bg-red-600 hover:bg-red-700 p-3 rounded-lg text-center">
                                View More
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
const selectedGenre = ref('');
const { data: movies, error } = useFetch('http://127.0.0.1:8000/api/series');
if (error) {
    console.error('Error fetching movies:', error);
}

const genres = computed(() => {
    if (!movies.value) return [];
    return [...new Set(movies.value.map(movie => movie.genre))];
});

const filteredMovies = computed(() => {
    if (!movies.value) return [];
    if (!selectedGenre.value) return movies.value;
    return movies.value.filter(movie => movie.genre === selectedGenre.value);
});

</script>


<style>
/* Add any additional styles here */
</style>