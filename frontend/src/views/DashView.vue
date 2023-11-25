<script setup>
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const firstView = ref(true);
const secondView = ref(true);
const thirdView = ref(true);
const fourthView = ref(true);

const subs = ref([
  "cscareerquestions",
  "csmajors",
  "devops",
  "learnprogramming",
]);

const subreddits = ref([]);

async function fetchSubreddit() {
  var requestingSubs =
    subs.value[0] +
    "+" +
    subs.value[1] +
    "+" +
    subs.value[2] +
    "+" +
    subs.value[3];
  await axios.get("/subreddits/" + requestingSubs).then((response) => {
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

function view(index) {
  if (index === 0) {
    return firstView.value;
  } else if (index === 1) {
    return secondView.value;
  } else if (index === 2) {
    return thirdView.value;
  } else {
    return fourthView.value;
  }
}

function edit(index) {
  console.log(index);
  if (index === 0) {
    firstView.value = !firstView.value;
  } else if (index === 1) {
    secondView.value = !secondView.value;
  } else if (index === 2) {
    thirdView.value = !thirdView.value;
  } else {
    fourthView.value = !fourthView.value;
  }
}

onBeforeMount(() => {
  fetchSubreddit();
});
</script>

<template>
  <div class="grid grid-cols-4 my-4">
    <div v-for="(subreddit, index) in subreddits.subreddits">
      <div
        class="flex flex-row justify-between items-center py-4 mb-2 mx-1 rounded-3xl bg-secondary"
      >
        <div v-if="view(index)" class="flex justify-start w-1/3 text-xl pl-2">
          r/{{ subreddit[index].sub }}
        </div>
        <div v-else class="flex justify-start w-1/3 text-xl pl-2">
          <input v-model="subs[index]" class="rounded-md" />
          <button @click="saveChanges">Save</button>
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
