<template>
    <section class="products">
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
import BaseProduct from '@/components/BaseProduct.vue'

export default {
  name: 'ProductsList',
  components: {
    BaseProduct,
  }
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
