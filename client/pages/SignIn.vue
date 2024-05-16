<template>
    <div
        class="container bg-[url('@/assets/img/background_netflix.jpg')] h-screen bg-cover bg-no-repeat max-md:bg-black max-md:w-[100%] max-md:h-[100%]">
        <div class="form-container w-[30%] h-[65%]  bg-black">
            <h2>Sign Up</h2>
            <form @submit.prevent="signup">
                <label for="username">Email or phone number</label>
                <input type="text" id="username" v-model="username" required>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
                <label for="confirmPassword">Confirm Password</label>
                <input type="password" id="confirmPassword" v-model="confirmPassword" required>
                <button type="submit">Sign Up</button>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            confirmPassword: ''
        };
    },
    methods: {
        signup() {

            if (this.password !== this.confirmPassword) {
                alert("Passwords do not match!");
                return;
            }

            // Implement signup logic here, e.g., send signup request to backend
            console.log('Signing up with:', this.username, this.password);
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
    max-width: 400px;
    padding: 20px;
    border-radius: 8px;
    background-color: black;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
    color: white;

}

.form-container h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-container label {
    display: block;
    margin-bottom: 8px;
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