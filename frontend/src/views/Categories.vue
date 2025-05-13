<template>
    <div class="h-screen flex justify-center">
        <div class="w-3/4 h-auto p-2">
            <h2 class="text-3xl">Categories</h2>
            <div class="text-lg">
                <form class="my-4">
                    <div class="">
                        <input v-model="searchTerm" type="text" placeholder="Search" class="bg-gray-300 w-full shadow-m">
                    </div>
                </form>
            </div>
            <div v-if="filtered.length > 0" class="w-full p-2 grid grid-cols-4 gap-4">
                <router-link 
                    v-for="category in filtered" 
                    :key="category"
                    :to="{ path: '/', query: { page: 1, category: category } }" 
                    class="mb-4"
                >
                    <p class="hover:opacity-50">{{ category }}</p>
                </router-link>
            </div>
            <div v-else>
                <div v-for="category in categories.value" :key="category" class="mb-4">
                    <p class="hover:opacity-50">{{ category }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from '../axios';

const categories = ref([])
const searchTerm = ref("")

onMounted(async() => {
    const res = await axios.get(`/categories`)
    categories.value = res.data
})

const filtered = computed(() => {
    if (!searchTerm.value){
        return categories.value
    } 
    return categories.value.filter(cat => cat.toLowerCase().includes(searchTerm.value.toLowerCase()))
})


</script>