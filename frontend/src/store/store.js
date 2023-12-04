import { defineStore } from "pinia";

export const useUserStore = defineStore("user", () => {
  const id = ref(0);
  const name = ref("");

  const getId = computed(() => id.value);
  const getName = computed(() => name.value);

  function setId(newId) {
    id.value = newId;
  }

  function setName(newName) {
    name.value = newName;
  }

  return { count, name, getId, getName, setId, setName };
});