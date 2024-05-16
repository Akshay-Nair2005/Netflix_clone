<template>
    <footer class="footer mt-24">
        <div class="footer-content">
            <div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Movies</a></li>
                    <li><a href="#">Series</a></li>
                    <li><a href="#">Help</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Follow Us</h4>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Instagram</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Legal</h4>
                <ul>
                    <li><a href="#">Terms of Use</a></li>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Cookie Policy</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Your Netflix Clone. All rights reserved.</p><br>
            <p>~Akshay Nair.</p>
        </div>
        <div class="flex-row-reverse flex">
            <Scrollup />
        </div>
    </footer>
</template>

<style scoped>
.footer {
    background-color: #111;
    color: #ddd;
    padding: 40px 20px;
    text-align: center;
    /* height: 100vh; */
}

.footer-content {
    display: flex;
    justify-content: space-between;
}

.footer-section {
    flex: 1;
    margin: 0 10px;
}

.footer-section h4 {
    margin-bottom: 10px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 5px;
}

a {
    color: #ddd;
    text-decoration: none;
}

a:hover {

    color: red;
}

.footer-bottom {
    margin-top: 20px;
}
</style>