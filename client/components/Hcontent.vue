<template>
    <div class="pt-[18%] pl-4 w-screen">
        <h1 class="text-[36px] text-red-600 font-serif font-bold">Trending Now</h1>
        <h1 class="text-[36px] text-white font-serif font-bold">Kungfu Panda</h1>
        <div class="flex">
            <img :src="star" :alt="name" />
            <p class="text-white text-[18px] m-4">8.0</p>
        </div>

        <p class="text-white text-[20px] w-[30%]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur
            optio
            mollitia voluptatibus. Nihil atque delectus veniam ex maxime aspernatur ipsam!</p>
    </div>
</template>

<script>
export default {
    props: {
        star: String,
        name: String
    }
}
</script>

<style></style>
