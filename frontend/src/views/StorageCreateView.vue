<template>
    <section class="storage-create">
        <button class="button add-button" @click="showForm = true">добавить склад</button>
            <form class="create-form" v-if="showForm" @submit.prevent="createStorage">
                <div class="create-form__item">
                    <label for="title">название</label>
                    <input type="text" name="title" v-model="title">
                </div>
                <div class="create-form__item">
                    <label for="address">адрес</label>
                    <input type="text" name="address" v-model="address">
                </div>
                <div class="create-form__item">
                    <label for="phone">номер телефона</label>
                    <input type="text" name="phone" v-model="phone_number">
                </div>
                <div class="create-form__item">
                    <label for="capacity">вместимость</label>
                    <input type="text" name="capacity" v-model="capacity">
                </div>
                <div class="buttons">
                    <button class="button" type="submit">добавить</button>
                    <button class="button negative-empty-button" type="button" @click="showForm = false">отменить</button>
                </div>
            </form>
    </section>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            showForm: false,
            title: "",
            address: "",
            phone_number: "",
            capacity: 0,
            current_stock: 0,
            is_full: 0,
        };
    },
    methods: {
        async createStorage() {
            try {
                const response = await axios.post("/api/v1/storages/", {
                    title: this.title,
                    address: this.address,
                    phone_number: this.phone_number,
                    capacity: this.capacity,
                    current_stock: this.current_stock,
                    is_full: this.is_full
                })
                console.log("storage created:", response.data)
                this.showForm = false
                this.title = ""
            } catch (error) {
                console.error("error:", error.response.data)
            }
        }
    }
}
</script>

<style scoped>
.storage-create {
    margin: 1rem 0;
}

.create-form .create-form__item {
    display: flex;
    max-width: 200px;
    flex-direction: column;
}

.create-form .create-form__item + .create-form__item {
    margin-top: 1rem;
}

.create-form__item input {
    border: none;
    outline: none;
    border-bottom: 1px solid #19a219;
}

.buttons {
    display: flex;
    gap: 0.5rem;
}
</style>
