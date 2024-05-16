<template>
    <h1 class="text-red-600 text-center text-[36px] mt-8 font-serif" id="help">Help</h1>
    <div class="help-page">
        <div class="help-content">
            <h2>Help</h2>
            <p>If you need any assistance or have questions about our service, please feel free to contact us:</p>
            <ul>
                <li>Email: support@yournetflixclone.com</li>
                <li>Phone: 9321144030</li>
                <li>FAQs: <router-link to="">Frequently Asked Questions</router-link></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    // You can add data, methods, etc. here if needed
};
</script>

<style scoped>
.help-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
}

.help-content {
    text-align: center;
    width: 80%;
    height: 60%;
    padding: 40px;
    font-size: 22px;
    background-color: #111;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.help-content h2 {
    color: #fff;
    margin-bottom: 20px;
}

.help-content p {
    color: #ddd;
    margin-bottom: 20px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    color: #ddd;
    margin-bottom: 10px;
}

a {
    color: #e50914;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>