<template>
  <div
    class="flex flex-row p-2 justify-between items-center w-full border-b-[1px] lg:px-20"
  >
    <RouterLink to="/" class="flex items-center text-xl font-bold">
      <img src="../../assets/dreddit.png" class="pr-3" />
      reddit dashboard
    </RouterLink>
    <div class="block w-auto">
      <ul
        class="font-medium flex p-4 border-gray-100 rounded-lg md:space-x-8 mt-0 border-0 bg-white"
      >
        <li>
          <RouterLink
            to="/dash"
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
