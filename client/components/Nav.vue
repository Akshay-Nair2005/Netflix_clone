<template>
    <div class="w-[98.5%] flex flex-wrap p-5 flex-col md:flex-row items-center opacity-8 bg-black">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
            <div class="w-[100%]">
                <img src="@/assets/img/netflix.png" alt="logo" class="h-10">
            </div>
        </a>
        <nav class="md:ml-auto md:mr-auto  mr-auto flex text-white">
            <a class="mr-5 hover:text-red-700 cursor-pointer" @click="scrollToSection('movies')">Movies</a>
            <a class="mr-5 hover:text-red-700 cursor-pointer" @click="scrollToSection('series')">Series</a>
            <a class="mr-5 hover:text-red-700 cursor-pointer" @click="scrollToSection('help')">Help</a>
            <a class="mr-5 hover:text-red-700 cursor-pointer" @click="scrollToSection('contact')">Contact Us</a>
        </nav>

        <NuxtLink to="./SignIn" class='bg-red-600  p-3 text-white md:text-lg rounded-md'>
            Sign In
        </NuxtLink>
    </div>
</template>

<script>
export default {
    name: "Nav",
    data() {
        return {
            isAuthenticated: false, // Set this based on your authentication state
        };
    },
    methods: {
        scrollToSection(sectionId) {

            const targetSection = document.getElementById(sectionId);
            if (targetSection) {

                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        },
    }
}
</script>

<style lang="scss" scoped></style>
