<template>
    <section class="storages">
        <!-- {{products}} -->
        <!-- <div class="products" v-for="product in products" v-bind:key="product.id"> -->
        <!--     <p class="storage__title">{{ product.title }}</p> -->
        <!-- </div> -->
        <div class="storage" v-for="storage in storages" v-bind:key="storage.id">
            <p class="storage__title">{{ storage.title }}</p>
            <div class="storage__infos">
                <div class="storage__info">
                    <p class="info__title">описание</p>
                    <p>{{ storage.description }}</p>
                </div>
                <div class="storage__info">
                    <p class="info__title">адрес</p>
                    <p>{{ storage.address }}</p>
                </div>
                <div class="storage__info">
                    <p class="info__title">номер телефона</p>
                    <p>{{ storage.phone_number }}</p>
                </div>
                <div class="storage__info">
                    <p class="info__title">вместимость</p>
                    <p>{{ storage.capacity }}</p>
                </div>
                <div class="storage__info">
                    <p class="info__title">текущая заполненность</p>
                    <p>{{ storage.current_stock }}</p>
                </div>
                <div class="storage__info">
                    <p class="info__title">заполнен</p>
                    <p>{{ storage.is_full }}</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: "StoragesList",
    data() {
        return {
            storages: [],
            products: [],
        }
    },
    mounted() {
        axios.get("api/v1/storages/")
            .then(response => {
                this.storages = response.data;
            })
            .catch(error => {
                console.error(error);
            })
        axios.get("api/v1/products/")
            .then(response => {
                this.products = response.data;
            })
            .catch(error => {
                console.error(error);
            })
    },
}
</script>

<style scoped>
.storages {
    display: flex;
    gap: 2rem;
}

.storage {
    border: 2px solid #19a219;
    border-radius: 1rem;
    padding: 1rem;
}

.storage .storage__title {
    font-size: 1.25rem;
    font-weight: 700;
}


.storage .storage__infos {
    margin: 1rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.storage__infos .storage__info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.storage__info .info__title {
    font-weight: 700;
    font-size: 0.95rem;
}
</style>
