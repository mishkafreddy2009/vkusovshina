<template>
    <footer>
        <p>хотите сотрудничать? <a href="#">стать поставщиком</a>.</p>
        <p>&copy; вкусовщина, 2024</p>
    </footer>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "TheFooter",
})
</script>

<style scoped>
footer {
    display: flex;
    justify-content: space-between;
    font-size: 0.75rem;
    margin: 2rem 1rem 1rem 1rem;
    position: relative;
    bottom: 0;
}

footer a {
    text-decoration: underline;
}
</style>
