module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss"),
    require("autoprefixer")({
      overrideBrowserslist: ["defaults and last 4 versions"],
    }),
  ],
};
