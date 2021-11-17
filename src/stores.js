import { writable } from "svelte/store";

export const isAuthenticated = writable(false);
export const user = writable("");
export const csrf = writable("");
export const isPosting = writable(false);
export const isFromRegister = writable(false);
