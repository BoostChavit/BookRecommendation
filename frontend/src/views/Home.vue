<template>
    <div>
      <div class="h-screen flex justify-center">
        <div class="w-3/4 h-auto p-2 flex-row justify-center items-center">
          <div class="mb-4">
            <span class="text-4xl">Result</span>
          </div>
          <div v-if="books.length > 0" class="grid grid-cols-3 gap-4">
            <router-link
              v-for="book in books"
              :key="book.id"
              :to="`/book/${book.id}`"
              class="h-auto block hover:shadow-xl transition"
            >
              <div class="h-60 flex justify-center bg-gray-200 overflow-hidden">
                <img :src="book.image_link" referrerpolicy="no-referrer" loading="lazy" class="h-full object-contain" />
              </div>
              <p class="text-lg font-bold p-2">{{ book.title }}</p>
              <p class="text-base p-2">By {{ book.author }}</p>
            </router-link>
            <div class="col-span-3 my-3">
              <hr class="w-full my-3">
              <div class="flex justify-center p-2">
                <button @click="currentPage -= 1" :disabled="currentPage === 1" class="">prev</button>
                <form class="mx-4" @submit.prevent="fetchBooksByInput()">
                  <input type="text" v-model="inputPage" class="border border-black-500 w-10 text-center">
                  <span> / {{ totalPage }}</span>
                </form>
                <button @click="currentPage += 1" :disabled="currentPage >= totalPage" class="">next</button>
              </div>
            </div>
          </div>
          <div v-else class="text-center text-red-500">
            <span class="text-4xl">No books found</span>
          </div>
        </div>
      </div>
    </div>  
  </template>
  
  
  <script setup>
  import {ref, onMounted, watch} from 'vue';
  import axios from '../axios';
  import { useRoute, useRouter } from 'vue-router';
  
  const route = useRoute()
  const router = useRouter()

  const books = ref([])
  const totalPage = ref(0)
  const currentPage = ref(parseInt(route.query.page) || 1)
  const category = ref(route.query.category || '')
  const inputPage = ref(currentPage.value)

  const fetchBooksByInput = () => {
    const page = parseInt(inputPage.value)
    console.log("fetchbyinput")
    if (!isNaN(page) && page >= 1 && page <= totalPage.value) {
      currentPage.value = page
    }
    else {
      inputPage.value = currentPage.value
    }
  }

  const fetchBooks = async () => {
    try {
      console.log("in fetchbooks")
      const response = await axios.get('/books', {
        params: {
          page: currentPage.value,
          offset: 9,
          category: category.value
        }
      })
      books.value = response.data.data
      totalPage.value = response.data.totalPage
      currentPage.value = response.data.page

    } catch (error) {
      console.log(error)
    }
  }

  watch(currentPage, (newPage) => {
    if (category.value === ''){
      router.push({ query: { page: newPage } })
    } else {
      router.push({ query: { page: newPage, category: category.value } })
    }
    inputPage.value = newPage
    fetchBooks()

  })

  watch(category, (newCategory) => {
    fetchBooks()
  })

  watch(() => route.query, (query) => {
    currentPage.value = parseInt(query.page) || 1
    category.value = query.category || ''
    inputPage.value = currentPage.value
  })

  onMounted(() => {
    fetchBooks()
  })

  </script>