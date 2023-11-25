<template>
  <h1
    class="mt-20 mb-4 text-4xl font-bold tracking-tight text-text lg:font-extrabold lg:text-6xl lg:leading-none lg:text-center xl:px-36 lg:mb-7"
  >
    One dashboard to follow your favorite subreddits
  </h1>
  <p
    class="mb-10 text-lg font-normal text-gray-500 lg:text-center lg:text-xl xl:px-60"
  >
    Select up to four subreddits and check what's going on without having to open multiple tabs.
  </p>
  <div class="flex flex-col mb-8 md:flex-row lg:justify-center">
    <RouterLink
      to="/dash"
      class="text-white bg-primary hover:transition-transform font-medium rounded-lg text-base px-6 py-2.5 text-center md:mr-5 mb-3 md:mb-0 inline-flex items-center justify-center"
      >Give it a try</RouterLink
    >
    <RouterLink
      to="/register"
      class=" text-text bg-secondary hover:bg-gray-100 hover:text-blue-600 border border-gray-200 font-medium rounded-lg text-base px-6 py-2.5 text-center inline-flex justify-center items-center"
    >
      <div class="ml-2">Register</div>
    </RouterLink>
  </div>
</template>
