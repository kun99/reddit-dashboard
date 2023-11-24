/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: [],
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        text: "#231011",
        background: "#ffffff",
        primary: "#d14415",
        secondary: "#c4d6e4",
        accent: "#331f0b",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
