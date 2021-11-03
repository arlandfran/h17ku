import "./global.css";
import HMR from "@roxi/routify/hmr";
import App from "./App.svelte";
import { setup } from "svelte-match-media";

setup();

const app = HMR(App, { target: document.body }, "routify-app");

export default app;
