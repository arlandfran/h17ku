const colors = require("tailwindcss/colors");

module.exports = {
  mode: "jit",
  darkMode: "class",
  theme: {
    colors: {
      white: colors.white,
      black: colors.black,
      gray: colors.trueGray,
      red: colors.red,
      green: colors.emerald,
      yellow: colors.amber,
      blue: colors.sky,
      rose: colors.rose,
    },
    deliciousHamburgers: {
      size: "28px",
      color: "#000",
      colorLight: "#fff8f4",
      padding: "0px",
      animationSpeed: 1.5,
    },
    extend: {
      spacing: {
        192: "42rem",
      },
    },
  },
  variants: {
    extend: {
      cursor: ["disabled"],
      textDecoration: ["disabled"],
    },
  },
  plugins: [require("tailwindcss-delicious-hamburgers")],
  purge: ["./index.html", "./src/**/*.svelte", "./src/**/*.css"],
};
