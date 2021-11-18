import { writable } from "svelte/store";

export const isAuthenticated = writable(false);
export const user = writable("");
export const csrf = writable("");
export const updatePosts = writable(false);
export const isFromRegister = writable(false);
export const filter = writable("popular");
export const updateComments = writable(false);
