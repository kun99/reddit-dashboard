<script setup>
import { ref, onBeforeMount } from "vue";

const username = ref("");
const password = ref("");

</script>

<template>
  <div class=" h-96 flex items-center justify-center">
    <div class="bg-white p-8 rounded shadow-md w-96">
      <h2 class="text-2xl font-semibold mb-4">Register</h2>
      <form @submit.prevent="register">
        <div class="mb-4">
          <label
            for="username"
            class="block text-gray-600 text-sm font-medium mb-2"
            >Username</label
          >
          <input
            type="text"
            id="username"
            v-model="username"
            class="w-full p-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
          />
        </div>
        <div class="mb-4">
          <label
            for="password"
            class="block text-gray-600 text-sm font-medium mb-2"
            >Password</label
          >
          <input
            type="password"
            id="password"
            v-model="password"
            class="w-full p-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
          />
        </div>
        <button
          type="submit"
          class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
        >
          Register
        </button>
      </form>
    </div>
  </div>
</template>