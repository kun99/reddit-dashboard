<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const followedSubreddits = ref(["soccer", "worldnews", "coys", "fitness"]);
const subreddits = ref([]);

async function fetchSubreddit() {
  var subs = "";
  followedSubreddits.value.forEach(sub => {
    subs = subs+sub+","
  });
  await axios
    .get("/subreddits/" + subs)
    .then((response) => {
      subreddits.value = response.data;
      console.log(subreddits.value.subreddits);
    });
}

async function deleteSubreddit(subreddit){
  var newSubreddits = [];
  followedSubreddits.value.forEach(sub => {
    if(subreddit!==sub){
      newSubreddits.push(sub);
    }
  });
  followedSubreddits.value = newSubreddits;
  fetchSubreddit();
}

onBeforeMount(() => {
  fetchSubreddit();
});
</script>

<template>
  <div class="flex justify-center text-2xl mt-5">Reddit Dashboard</div>
  <div class="grid grid-cols-4 py-8">
    <div v-for="(subreddit, index) in subreddits.subreddits">
      <div class="flex flex-row pb-4">
        <div class="flex justify-center w-1/3"></div>
        <div class="flex justify-center w-1/3">r/{{followedSubreddits[index]}}</div>
        <div class="flex justify-end w-1/3">
          <p
            class="text-stone-400 rounded-md w-5 flex justify-center cursor-pointer"
            @click="deleteSubreddit(followedSubreddits[index])"
          >
            x
          </p>
        </div>
      </div>
      <div class="bg-gray-100">
        <div v-for="submission in subreddit">
          <a
            v-bind:href="submission.url"
            target="_blank"
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
