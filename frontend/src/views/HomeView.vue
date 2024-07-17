<template>
  <div class="home">
      <TheHeader />
      <main>
          <ProductsList />
      </main>
      <TheFooter />
  </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from '@/components/TheHeader.vue'
import ProductsList from '@/components/ProductsList.vue'
import TheFooter from '@/components/TheFooter.vue'

export default {
  name: 'HomeView',
  components: {
    TheHeader,
    ProductsList,
    TheFooter,
  }
}
</script>

<style scoped>
main {
    margin: 2rem 1rem;
}
</style>
