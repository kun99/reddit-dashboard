<script setup>
import { RouterLink, RouterView } from "vue-router";
import AppBar from "./components/AppBar.vue";
import { useUserStore } from "@/store/store.js";

</script>

<template>
  <nav class="bg-background">
    <AppBar />
  </nav>
  <main class="lg:mx-20">
    <RouterView />
  </main>
</template>
