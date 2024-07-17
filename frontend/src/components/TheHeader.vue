<template>
    <header>
        <h1>Вкусовщина</h1>
        <div class="search-box">
            <svg class="search-box__icon">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M11 7C11 9.20914 9.20914 11 7 11C4.79086 11 3 9.20914 3 7C3 4.79086 4.79086 3 7 3C9.20914 3 11 4.79086 11 7ZM11.0747 12.4889C10.7294 12.1436 10.1889 12.1068 9.75528 12.3314C8.93019 12.7586 7.99328 13 7 13C3.68629 13 1 10.3137 1 7C1 3.68629 3.68629 1 7 1C10.3137 1 13 3.68629 13 7C13 7.99328 12.7586 8.93019 12.3314 9.75528C12.1068 10.1889 12.1436 10.7294 12.4889 11.0747L14.7071 13.2929C15.0976 13.6834 15.0976 14.3166 14.7071 14.7071C14.3166 15.0976 13.6834 15.0976 13.2929 14.7071L11.0747 12.4889Z" fill="currentColor"></path>
            </svg>
            <input class="search-box__input" type="text" placeholder="искать во вкусовщине">
        </div>
        <div class="cart">
            <a class="cart__button" href="">
                <svg class="cart__icon" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#19A219">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
                </svg>
            </a>
        </div>
    </header>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "TheHeader",
})
</script>

<style scoped>
header {
    display: flex;
    align-items: center;
    border-radius: 1rem;
    margin: 1rem;
    gap: 2rem;
}

h1 {
    font-weight: 400;
    text-transform: lowercase;
    font-size: 2rem;
}

.search-box {
    width: 100%;
    display: flex;
    align-items: center;
    border-radius: 1rem;
    background-color: #f5f5f5;
}

.search-box__icon {
    margin-left: 1rem;
    margin-right: 0.5rem;
    width: 16px;
    height: 16px;
    color: #a2a2a2;
}

.search-box__input {
    padding: 1rem 1rem 1rem 0;
    width: 100%;
    background-color: #f5f5f5;
    border: none;
    outline: none;
    border-radius: 1rem;
}

.search-box__input::placeholder {
    color: #a2a2a2;
}

.cart {
    background-color: #f5f5f5;
    border-radius: 1rem;
    padding: 0rem 0.5rem;
}

.cart__icon {
    width: 48px;
    height: 48px;
}

</style>
