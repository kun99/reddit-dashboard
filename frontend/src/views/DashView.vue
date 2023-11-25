<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const followedSubreddits = ref([
  "learnprogramming",
  "cscareerquestions",
  "csmajors",
  "devops",
]);

const subreddits = ref([]);

async function fetchSubreddit() {
  var subs = "";
  followedSubreddits.value.forEach((sub) => {
    subs = subs + sub + "+";
  });
  await axios.get("/subreddits/" + subs).then((response) => {
    subreddits.value = response.data;
    console.log(subreddits.value.subreddits);
  });
}

async function deleteSubreddit(subreddit) {
  var newSubreddits = [];
  followedSubreddits.value.forEach((sub) => {
    if (subreddit !== sub) {
      newSubreddits.push(sub);
    }
  });
  followedSubreddits.value = newSubreddits;
  fetchSubreddit();
  console.log(followedSubreddits.value);
}

onBeforeMount(() => {
  fetchSubreddit();
});
</script>

<template>
  <div class="grid grid-cols-4 my-4">
    <div v-for="(subreddit, index) in subreddits.subreddits">
      <div class="flex flex-row justify-between items-center py-4 mb-2 mx-1 shadow rounded-3xl bg-secondary">
        <div class="flex justify-start w-1/3 text-xl pl-2">
          r/{{ followedSubreddits[index] }}
        </div>
        <div class="flex justify-end w-1/3 items-center">
          <font-awesome-icon
            class="mt-2 mr-2 text-xs rounded-lg shadow"
            icon="fa-solid fa-pencil"

          />
          <p
            class="text-stone-400 rounded-lg w-5 flex justify-center cursor-pointer text-xl shadow" 
            @click="deleteSubreddit(followedSubreddits[index])"
          >
            x
          </p>
        </div>
      </div>
      <div v-for="submission in subreddit">
        <a
          v-bind:href="submission.url"
          target="_blank"
          class="h-48 block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100"
        >
          <p
            class="h-28 mb-4 overflow-auto text-ellipsis text-xl font-bold tracking-tight text-gray-900"
          >
            {{ submission.title }}
          </p>
          <p class="font-normal text-gray-700">
            Upvotes: {{ submission.upvotes }}
          </p>
        </a>
      </div>
    </div>
  </div>
</template>
