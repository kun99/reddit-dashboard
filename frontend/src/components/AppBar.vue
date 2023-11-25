<template>
  <div
    class="flex flex-row p-2 justify-between items-center w-full border-b-[1px] lg:px-20"
  >
    <RouterLink to="/" class="flex items-center text-xl font-bold">
      <img src="../../assets/dreddit.png" class="pr-3" />
      reddit dashboard
    </RouterLink>
    <div class="hidden w-full md:block md:w-auto">
      <ul
        class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white"
      >
        <li>
          <RouterLink
            to="/dash#"
            class="block py-2 px-3 text-text md:hover:text-primary md:p-0"
            aria-current="page"
            >Dashboard</RouterLink
          >
        </li>
        <li>
          <RouterLink
            to="/login"
            class="block py-2 px-3 text-text md:hover:text-primary md:p-0"
            >Login</RouterLink
          >
        </li>
      </ul>
    </div>
  </div>
</template>
