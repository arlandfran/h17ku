<script>
  import { params, goto } from "@roxi/routify";
  import { onMount } from "svelte";
  import { createForm } from "svelte-forms-lib";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";
  import { loginSchema } from "../../schemas";

  const csrf = document.getElementsByName("csrf-token")[0].content;

  onMount(() => {
    if ($params.newUser) {
      toast.push("new account created!", {
        initial: 1,
        reversed: true,
        intro: { y: 64 },
        theme: {
          "--toastMinHeight": "2rem",
          "--toastPadding": "0 0.5rem",
          "--toastBackground": "#48BB78",
          "--toastBarBackground": "transparent",
        },
      });
    }
  });

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: loginSchema,
    onSubmit: async (values) => {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrf,
        },
        credentials: "same-origin",
        body: JSON.stringify(values),
      });

      const result = await response.json();

      if (result.login) {
        $goto("/");
      } else if (!result.login && response.status === 401) {
        $errors.password = result.msg;
      } else if (!result.login && response.status === 404) {
        $errors.email = result.msg;
      } else if (
        response.status === 400 &&
        result.msg === "The CSRF token has expired."
      ) {
        toast.push("session has expired, please refresh the page", {
          initial: 1,
          reversed: true,
          intro: { y: 64 },
          theme: {
            "--toastMinHeight": "2rem",
            "--toastPadding": "0 0.5rem",
            "--toastBarBackground": "transparent",
          },
        });
      }
    },
  });
</script>

<h1 class="text-4xl font-bold dark:text-white">log in</h1>

<div class="w-full max-w-2xl min-w-xs dark:text-white">
  <form on:submit={handleSubmit} class="py-6">
    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> email</label>
      <input
        class:error={$errors.email}
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="email"
        type="email"
        placeholder="email address"
        on:change={handleChange}
        bind:value={$form.email}
        on:invalid|preventDefault
      />
      {#if $errors.email}
        <small class="py-2 text-xs text-red-600">{$errors.email}</small>
      {/if}
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> password </label>
      <input
        class:error={$errors.password}
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="password"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password}
      />
      {#if $errors.password}
        <small class="py-2 text-xs text-red-600">{$errors.password}</small>
      {/if}
    </div>

    <div class="flex justify-center">
      <button
        class="px-4 py-2 text-xl font-bold dark:text-white focus:outline-none focus:ring-black dark:ring-white focus:ring-2 disabled:line-through disabled:cursor-default"
        type="submit"
      >
        log in
      </button>
    </div>
  </form>
</div>

<Toast />

<style>
  .error {
    @apply border border-red-600 ring-red-600;
  }
</style>
