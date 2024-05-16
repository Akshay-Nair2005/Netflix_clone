<template>
    <h1 class="text-red-600 text-center text-[36px] mt-8 font-serif" id="contact">Contact Us</h1>
    <div class="contact-page">
        <div class="contact-form">
            <h2 class="text-[22px]">Contact Us</h2>
            <form @submit.prevent="submitForm" class="w-[100%] flex justify-between">

                <div class="w-[50%] ">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" v-model="formData.name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" v-model="formData.email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" v-model="formData.message" rows="4" required></textarea>
                    </div>
                    <button type="submit">Submit</button>
                </div>
                <div class="w-[40%] ">
                    <img src="@/assets/img/tv.png" alt="img" class="">
                </div>

            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            formData: {
                name: '',
                email: '',
                message: ''
            }
        };
    },
    methods: {
        submitForm() {
            alert('Form submitted:', this.formData);
            this.clearForm();
        },
        clearForm() {
            this.formData = {
                name: '',
                email: '',
                message: ''
            };
        }
    }
};
</script>

<style scoped>
.contact-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.contact-form {
    width: 80%;
    background-color: #111;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);

}

.contact-form h2 {
    color: #fff;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
    width: 100%;
}

label {
    color: #ddd;
}

input,
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #333;
    color: #fff;
}

button {
    width: 100%;
    padding: 12px;
    background-color: #e50914;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #d30812;
}
</style>