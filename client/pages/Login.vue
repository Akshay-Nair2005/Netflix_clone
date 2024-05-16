<template>
    <div
        class="container bg-[url('@/assets/img/background_netflix.jpg')] h-screen bg-cover bg-no-repeat max-md:bg-black max-md:w-[100%] max-md:h-[100%]">
        <div class="form-container w-[30%] h-[60%] ">
            <h2 class="text-[25px] font-serif font-bold">Login Page</h2>
            <form @submit.prevent="login">
                <label for="username">Email or phone number</label>
                <input type="text" id="username" v-model="username" required>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
                <button type="submit">Sign In</button>
            </form><br>
            <nuxt-link to="./SignIn" class="ml-20 font-bold text-white"><span
                    class="text-red-600 hover:text-red-700">Sign Up</span> For Registration</nuxt-link>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            userData: []
        };
    },
    async mounted() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/users/');
            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }
            const userData = await response.json();
            this.userData = userData;
        } catch (error) {
            console.error('Error fetching user data:', error);
        }
    },
    methods: {
        async login() {
            try {
                const user = this.userData.find(user => user.username === this.username && user.password === this.password);
                if (user) {
                    this.$router.push('/Netflix');
                } else {
                    alert('Invalid username or password');
                }
            } catch (error) {
                alert('An error occurred while logging in. Please try again later.');
                console.error('Login error:', error);
            }
        }
    }
}
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.form-container {
    width: 400px;
    background: #000;
    padding: 20px;
    border-radius: 8px;
    background-color: #000;
    opacity: 0.85;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
}

.form-container h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #fff;
}

.form-container label {
    display: block;
    margin-bottom: 8px;
    color: #fff;
}

.form-container input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.form-container button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 4px;
    background-color: #e50914;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.form-container button:hover {
    background-color: #c90d10;
}
</style>
