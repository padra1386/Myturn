/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "./base/templates/base/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          500: "#FF6363;",
          800: "#FF1313;",
        },
      },
      fontFamily: {
        dana: ["DANA", "cursive"],
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
