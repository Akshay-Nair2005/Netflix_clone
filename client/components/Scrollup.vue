<template>
    <div>
        <button @click="scrollToTop" class="bg-red-600 hover:bg-red-700 text-[25px] p-3 rounded-full">^</button>
    </div>
</template>

<script>
export default {
    methods: {
        scrollToTop() {
            // Scroll to the top of the page smoothly
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Smooth scrolling behavior
            });
        }
    }
}
</script>