<script setup>
import { RouterLink, RouterView } from "vue-router";
import AppBar from "./components/AppBar.vue";
</script>

<template>
  <nav class="bg-background">
    <AppBar />
  </nav>
  <main>
    <RouterView />
  </main>
</template>
