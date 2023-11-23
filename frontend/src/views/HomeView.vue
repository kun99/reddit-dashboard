<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const subreddits = ref([]);

async function fetchSubreddit() {
  await axios.get("/subreddits/" + "soccer,worldnews,coys,fitness").then((response) => {
    subreddits.value = response.data;
    console.log(subreddits.value.subreddits);
  });
}

onBeforeMount(() => {
  fetchSubreddit();
});
</script>

<template>
  <div class="flex justify-center text-2xl mt-5">
    Reddit Dashboard
  </div>
  <div class="grid grid-cols-4 py-4">
    <div v-for="subreddit in subreddits.subreddits">
      <div class="bg-gray-100">
        <div v-for="submission in subreddit">
          <a
            href=""
            class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100"
          >
            <p class="mb-2 text-xl font-bold tracking-tight text-gray-900">
              {{ submission.title }}
            </p>
            <p class="font-normal text-gray-700">
              Upvotes: {{ submission.upvotes }}
            </p>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
