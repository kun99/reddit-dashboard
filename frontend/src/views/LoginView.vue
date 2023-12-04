<script setup>
import { ref } from "vue";
import  router from "@/router/index.js";
import { useUserStore } from "@/store/store.js";

const email = ref("");
const password = ref("");

import { signInWithEmailAndPassword  } from "firebase/auth";
import { auth } from "../js/firebase.js";

function login() {
  signInWithEmailAndPassword(auth, email.value, password.value)
    .then((userCredential) => {
      const user = userCredential.user;
      const userStore = useUserStore();
      const { setId, setName } = userStore;
      console.log(user);
      setId(user.uid)
      setName(user.email)
      router.push('/dash')
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      console.log(errorCode + errorMessage);
    });
}
</script>

<template>
  <div class="h-96 flex items-center justify-center">
    <div class="bg-white p-8 rounded shadow-md w-96">
      <h2 class="text-2xl font-semibold mb-4">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label
            for="email"
            class="block text-gray-600 text-sm font-medium mb-2"
            >Email</label
          >
          <input
            type="text"
            id="email"
            v-model="email"
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
        <div class="pb-2">
          <RouterLink to="/register" class=" cursor-pointer text-sm"> Not registered? </RouterLink>
        </div>
        <button
          type="submit"
          class="bg-primary text-white px-4 py-2 rounded hover:bg-orange-600 focus:outline-none focus:ring focus:border-blue-300"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>
