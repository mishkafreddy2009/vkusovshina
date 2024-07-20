<template>
    <div class="dashboard">
        <StorageCreateView />
        <StoragesList />
    </div>
</template>

<script>
// @ is an alias to /src
import StoragesList from '@/components/StoragesList.vue'
import StorageCreateView from '@/views/StorageCreateView.vue'

export default {
  name: 'DashboardView',
  components: {
      StoragesList,
      StorageCreateView,
  }
}
</script>

<style scoped>
.dashboard {
    margin: 1rem;
}
</style>
