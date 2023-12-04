<template>
  <div class="flew-col md:flex-row lg:h-[600px]">
    <div class="md:inline-block md:w-3/5">
      <h1
        class="mt-20 mb-4 text-4xl text-text font-extrabold lg:text-6xl lg:mb-7"
      >
        <span
          class="text-transparent bg-clip-text bg-gradient-to-r to-orange-400 from-primary"
          >One</span
        >
        dashboard to view your favorite subreddits in
        <span
          class="text-transparent bg-clip-text bg-gradient-to-r to-orange-400 from-primary"
          >one</span
        >
        tab
      </h1>
      <p class="mb-10 text-lg font-normal text-gray-500 lg:text-xl">
        Select up to four subreddits and stay up to date without having to open
        multiple tabs.
      </p>
      <div class="flex-row mb-8 md:flex-row">
        <RouterLink
          to="/dash"
          class="text-white bg-primary hover:bg-orange-600 font-medium rounded-lg text-base px-6 py-2.5 text-center mr-5 mb-3 md:mb-0 inline-flex items-center"
          >Give it a try</RouterLink
        >
        <RouterLink
          to="/register"
          class="text-text bg-secondary hover:bg-gray-100 hover:text-primary border border-gray-200 font-medium rounded-lg text-base px-6 py-2.5 text-center inline-flex items-center"
        >
          <div class="ml-2">Register</div>
        </RouterLink>
      </div>
    </div>
    <div class="md:inline-block md:w-2/5">
      <video class="pt-10" src="../../assets/reddit dash.mp4" autoplay loop muted></video>
    </div>
  </div>
  <hr class="my-8 border-gray-200 mx-auto dark:border-gray-700" />
  <span class="block text-sm text-gray-500 text-center dark:text-gray-400"
    >2023
    <a href="https://github.com/kun99" class="hover:underline">Geon Kim</a></span
  >
</template>
