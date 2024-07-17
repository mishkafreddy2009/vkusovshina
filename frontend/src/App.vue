<template>
    <div id="app">
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<style>
.container {
    max-width: 1440px;
    margin: 0 auto;
    position: absolute;
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
</style>

