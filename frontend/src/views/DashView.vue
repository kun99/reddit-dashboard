<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const subs = ref([
  "cscareerquestions",
  "csmajors",
  "devops",
  "learnprogramming",
]);

const subreddits = ref([]);

async function fetchSubreddit() {
  if (subs.value[0] != "---") {
    var requestingSubs = "";
    requestingSubs = subs.value.filter((sub) => sub !== "---").join("+");
    await axios.get("/subreddits/" + requestingSubs).then((response) => {
      subreddits.value = response.data.subreddits;
      while (subreddits.value.length < 4) {
        subreddits.value.push(["nothing"]);
      }
    });
  } else {
    subreddits.value[0] = ["nothing"];
  }
}

async function deleteSubreddit(index) {
  var newSubreddits = [];
  var newSubmissions = [];
  var count = 0;
  for (let i = 0; i < 4; i++) {
    if (i != index) {
      newSubreddits.push(subs.value[i]);
      newSubmissions.push(subreddits.value[i]);
      count++;
    }
  }
  for (let i = count; i < 4; i++) {
    newSubreddits.push("---");
    newSubmissions.push(["none"]);
  }
  subs.value = newSubreddits;
  subreddits.value = newSubmissions;
}

function saveChanges() {
  fetchSubreddit();
}

function edit() {
  saveChanges();
}

onBeforeMount(() => {
  fetchSubreddit();
});
</script>

<template>
  <div class="grid grid-cols-4 my-4">
    <div v-for="(subreddit, index) in subreddits">
      <div
        class="flex flex-row justify-between items-center py-4 mb-2 mx-1 rounded-xl bg-slate-100"
      >
        <div class="flex justify-start w-1/3 text-xl pl-2">
          r/<input
            v-model="subs[index]"
            v-on:keyup.enter="saveChanges"
            class="rounded-md bg-slate-100"
          />
        </div>
        <div class="flex justify-end w-1/3 items-center">
          <button @click="edit(index)">
            <font-awesome-icon
              class="mt-2 mr-2 text-xs"
              icon="fa-solid fa-pencil"
            />
          </button>
          <p
            class="text-stone-400 flex justify-center cursor-pointer text-xl px-1 mr-2"
            @click="deleteSubreddit(index)"
          >
            x
          </p>
        </div>
      </div>
      <div v-for="submission in subreddit">
        <a
          v-bind:href="submission.url"
          target="_blank"
          v-if="submission.upvotes"
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
