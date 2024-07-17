import { createStore } from "vuex";

import storages from "./modules/storages";
import products from "./modules/products";

export default createStore({
    modules: {
        storages,
        products
    }
});
