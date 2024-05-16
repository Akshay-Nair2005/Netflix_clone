<template>
    <div class="bg-[url('@/assets/img/background_netflix.jpg')] h-screen bg-cover bg-no-repeat overflow-hidden">
        <div class="w-full h-full bg-black bg-opacity-50 ">

            <div class="flex justify-center items-center h-full w-full flex-col">
                <div class="text-white flex items-center flex-col">
                    <h1 class="text-[45px] font-bold ">
                        Unlimited movies, TV shows and more
                    </h1>
                    <h3 class="text-[25px]">Watch anywhere. Cancel anytime.</h3>
                    <p class="text-[25px]">
                        Ready to watch? Enter your email or mobile number to create or restart your membership
                    </p>
                </div><br /><br />
                <div class="flex gap-5 top-[50%] left-[28%]">
                    <NuxtLink
                        class="bg-red-600 hover:bg-red-700 w-40 h-12 p-3 text-center rounded-lg text-white font-bold"
                        to="./Login">
                        Get Started >
                    </NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
</script>

<style></style>