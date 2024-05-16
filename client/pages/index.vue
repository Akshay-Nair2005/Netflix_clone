<template>
    <div class="splash-screen">
        <img src="@/assets/img/netflix.png" alt="Netflix Logo" class="logo">
        <div class="loading-spinner"></div>
    </div>
</template>

<script>
export default {
    mounted() {

        setTimeout(() => {
            this.$router.push('/Homee');
        }, 3000);
    }
}
</script>

<style scoped>
.splash-screen {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    /* Set width to 100% of viewport width */
    background-color: #000;
    /* overflow-x: hidden; */
    /* Hide horizontal overflow */
}

.logo {
    width: 200px;
    /* Adjust the size of the logo as needed */
}

.loading-spinner {
    margin-top: 20px;
    width: 40px;
    height: 40px;
    border: 4px solid red;
    border-top: 4px solid transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>
