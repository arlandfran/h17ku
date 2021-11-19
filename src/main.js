import "./global.css";
import HMR from "@roxi/routify/hmr";
import App from "./App.svelte";
import { setup } from "svelte-match-media";

setup({
  desktop: "screen and (min-width: 769px)",
  mobile: "screen and (max-width: 768px)",
  smallMobile: "screen and (max-width: 425px)",
});

if (
  localStorage.theme === "dark" ||
  (!("theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  document.documentElement.classList.add("dark");
} else {
  document.documentElement.classList.remove("dark");
}

// Whenever the user explicitly chooses light mode
localStorage.theme = "light";

// Whenever the user explicitly chooses dark mode
localStorage.theme = "dark";

// Whenever the user explicitly chooses to respect the OS preference
localStorage.removeItem("theme");

const app = HMR(App, { target: document.body }, "routify-app");

export default app;
