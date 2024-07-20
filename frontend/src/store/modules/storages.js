import axios from "axios";

const state = {
    storages: null,
    storage: null
};

const getters = {
    stateStorages: state => state.storages,
    stateStorage: state => state.storage,
};

const actions = {
    async createStorage({dispatch}, storage) {
        await axios.post("api/v1/storages", storage);
        await dispatch("getStorages");
    },
    async getStorages({commit}) {
        let {data} = await axios.get("api/v1/storages");
        commit("setStorages", data);
    },
    // eslint-disable-next-line no-empty-pattern
    async updateStorage({}, storage) {
        await axios.patch("api/v1/storages/${storage.id}", storage.form);
    },
    // async viewStorage
    // async deleteStorage
};

const mutations = {
    setStorages(state, storages){
        state.storages = storages;
    },
    setStorage(state, storage){
        state.storage = storage;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
