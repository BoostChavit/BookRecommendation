<template>
<div v-if="book !== null" class="h-screen p-2">
    <div  class="h-2/3 flex">
        <div class="w-1/3 flex justify-center">
            <img :src="book.image_link" class="h-full object-contain shadow-md">
        </div>
        <div class="w-2/3 ">
            <h2 class="text-xl font-bold">{{ book.title }}</h2>
            <p>By: {{ book.author }}</p>
            <p>Category: {{ book.category }}</p>
            <hr class="my-4">
            <p>{{ book.description }}</p>
        </div>
    </div>
    <hr class="opacity-50 my-3">
    <div class="h-1/3 mt-5">
        <h2 class="text-xl font-bold">Related books</h2>
        <hr class="my-4">
        <div v-if="recommend_books !== null" class="flex flex-row justify-between h-32">
            <router-link
              v-for="recommend_book in recommend_books"
              :key="recommend_book.id"
              :to="`/book/${recommend_book.id}`"
              class="h-auto w-1/5 block hover:shadow-xl transition p-2"
            >
              <div class="h-60 flex justify-center bg-gray-200 overflow-hidden">
                <img :src="recommend_book.image_link" referrerpolicy="no-referrer" loading="lazy" class="h-full object-contain" />
              </div>
              <p class="text-lg font-bold p-2 truncate">{{ recommend_book.title }}</p>
              <p class="text-base p-2">By {{ recommend_book.author }}</p>
            </router-link>
        </div>
        <div v-else>
            <p>No recommendation</p>
        </div>
    </div>
</div>
<div v-else>
    <h1>Not Found</h1>
</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from '../axios';
import { useRoute } from 'vue-router'

const book = ref({})
const recommend_books = ref([])
const route = useRoute()

const fetchBooks = async(id) => {
    try {
        const res = await axios.get(`/book/${id}`)
        if(res.status === 200) {
            book.value = res.data
        } else {
            book.value = null
        }

        const recommend_res = await axios.get(`/recommend`, {
            params: {
                id: id
            }
        })
        if (recommend_res.status === 200) {
            recommend_books.value = recommend_res.data
        } else {
            recommend_books.value = null
        }
    } catch (error) {
      console.error('Error fetch fail')
    }
}

onMounted(() => {
    fetchBooks(route.params.id)
}) 

watch(() => route.params.id, (new_id) => {
    fetchBooks(new_id)
})

</script>