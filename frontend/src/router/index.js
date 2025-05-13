import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import Categories from "../views/Categories.vue"


const routes = [
    {path: "/", component: Home},
    {path: "/categories", component: Categories},
    {path: "/book/:id", component: () => import("../views/BookDetail.vue")},
]

export default createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() {
        return { top: 0 }
    }
})

