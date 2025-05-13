<script>

</script>

<template>
    <nav class="bg-white flex justify-items-center p-4 mb-6 h-30 border border-black-200 sticky top-0">
        <div class="w-1/4 p-4">
            <RouterLink :to="{ path: '/', query: { page: 1 } }"><img src="/src/assets/images.jpeg" alt="logo" class="h-full" ></RouterLink>
            
        </div>
        <div class="w-1/2 p-4">
            <ul class="w-full flex justify-items-center justify-between">
                <li class="m-2"><RouterLink :to="{ path: '/', query: { page: 1 } }">Home</RouterLink></li>
                <li class="m-2"><RouterLink to="/categories">Category</RouterLink></li>
            </ul>
        </div>
    </nav>
</template>