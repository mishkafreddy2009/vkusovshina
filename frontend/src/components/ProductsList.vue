<template>
    <section class="products">
        <!-- <li v-for="storage in storages" v-bind:key="storage.id">{{ storage }}</li> -->
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
        <BaseProduct />
    </section>
</template>

<script>
import axios from 'axios';
import BaseProduct from '@/components/BaseProduct.vue';

export default {
    name: "ProductsList",
    components: {
        BaseProduct
    },
    data() {
        return {
            storages: []
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
    },
}
</script>

<style scoped>
.products {
    margin: 2rem 0;
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 0.75rem;
}
</style>
