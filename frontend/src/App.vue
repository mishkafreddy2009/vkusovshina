<template>
    <!-- <div class="container"> -->
        <router-view/>
    <!-- </div> -->
</template>

<style>
.container {
    max-width: 1440px;
    margin: 0 auto;
}

*,
*::after,
*::before {
    box-sizing: border-box;
}

* {
    margin: 0;
    padding: 0;
    font: inherit;
}

body {
    display: flex;
    color: #555;
    flex-direction: column;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    line-height: 1;
    letter-spacing:-0.05rem;
}

img,
picture,
video,
svg {
    display: block;
    max-width: 100%;
}

h1 {
    text-wrap: balance;
}

p,
li {
    max-width: 65ch;
    text-wrap: pretty;
    list-style: none;
}

a {
    text-decoration: none;
    color: inherit;
}

.button {
    background: none;
    outline: none;
    border: none;
    background-color: #19a219;
    color: #fff;
    padding: 0.5rem;
    border-radius: 1rem;
    cursor: pointer;
    align-items: center;
    display: flex;
    margin: 1rem 0;
}

.add-button::after {
    content: "+";
    margin-left: 0.1rem;
    font-size: 1.8rem;
}

.positive-empty-button {
    color: #19a219;
    background-color: transparent;
    border: 1px solid #19a219;
}

.negative-empty-button {
    color: red;
    background-color: transparent;
    border: 1px solid red;
}
</style>

