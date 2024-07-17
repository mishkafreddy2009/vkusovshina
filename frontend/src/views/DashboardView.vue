<template>
    <div class="dashboard">
        <BaseStorage />
    </div>
</template>

<script>
// @ is an alias to /src
import BaseStorage from '@/components/BaseStorage.vue'

export default {
  name: 'DashboardView',
  components: {
      BaseStorage,
  }
}
</script>

<style scoped>
main {
    margin: 2rem 1rem;
}
</style>
