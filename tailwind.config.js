const colors = require("tailwindcss/colors");

module.exports = {
  darkMode: "class",
  theme: {
    colors: {
      white: colors.white,
      black: colors.black,
      gray: colors.trueGray,
    },
    deliciousHamburgers: {
      size: "28px",
      color: "#000",
      colorLight: "#fff8f4",
      padding: "0px",
      animationSpeed: 1.5,
    },
  },
  plugins: [require("tailwindcss-delicious-hamburgers")],
  purge: ["./src/**/*.svelte", "./src/**/*.css"],
};
