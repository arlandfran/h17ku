<script>
  import { goto } from "@roxi/routify";
  import { createForm } from "svelte-forms-lib";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";
  import { registerSchema } from "../../schemas";
  import { csrf, isFromRegister } from "../../stores";

  let passwordsMatch;

  const { form, errors, isValid, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: "",
      username: "",
      password: "",
      password2: "",
    },
    validationSchema: registerSchema,
    onSubmit: async (values) => {
      if (values.password === values.password2) {
        passwordsMatch = true;

        const response = await fetch("/api/auth/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": $csrf,
          },
          credentials: "same-origin",
          body: JSON.stringify(values),
        });

        const result = await response.json();

        if (response.status === 201) {
          $goto("../login");
          $isFromRegister = true;
        } else if (response.status === 409) {
          if (result.errorField === "email") {
            $errors.email = result.msg;
          } else if (result.errorField === "username") {
            $errors.username = result.msg;
          }
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
      } else {
        passwordsMatch = false;
      }
    },
  });
</script>

<h1 class="title">create your account</h1>

<div class="w-full max-w-2xl min-w-xs">
  <form on:submit={handleSubmit} class="py-6">
    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> email </label>
      <input
        class:error={$errors.email}
        class="px-3 py-2 w-full leading-tight rounded border border-black appearance-none dark:shadow-lg focus:outline-none focus:ring-black dark:ring-white focus:ring-1 dark:focus:ring-2 dark:bg-gray-700 dark:border-none"
        id="email"
        type="email"
        placeholder="email address"
        on:change={handleChange}
        bind:value={$form.email}
        on:invalid|preventDefault
      />
      {#if $errors.email}
        <small class="text-error">{$errors.email}</small>
      {/if}
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> username </label>
      <input
        class:error={$errors.username}
        class="px-3 py-2 w-full leading-tight rounded border border-black appearance-none dark:shadow-lg focus:outline-none focus:ring-black dark:ring-white focus:ring-1 dark:focus:ring-2 dark:bg-gray-700 dark:border-none"
        id="username"
        type="text"
        placeholder="username"
        on:change={handleChange}
        bind:value={$form.username}
      />
      {#if $errors.username}
        <small class="text-error">{$errors.username}</small>
      {/if}
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> password </label>
      <input
        class:error={$errors.password}
        class="px-3 py-2 w-full leading-tight rounded border border-black appearance-none dark:shadow-lg focus:outline-none focus:ring-black dark:ring-white focus:ring-1 dark:focus:ring-2 dark:bg-gray-700 dark:border-none"
        id="password"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password}
      />
      {#if $errors.password}
        <small class="text-error">{$errors.password}</small>
      {/if}
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> confirm password </label>
      <input
        class:error={$errors.password2}
        class="px-3 py-2 w-full leading-tight rounded border border-black appearance-none dark:shadow-lg focus:outline-none focus:ring-black dark:ring-white focus:ring-1 dark:focus:ring-2 dark:bg-gray-700 dark:border-none"
        id="password2"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password2}
      />
      {#if $errors.password2}
        <small class="py-2 text-xs font-bold text-red-600 dark:font-normal"
          >{$errors.password2}</small
        >
      {/if}
      {#if passwordsMatch === false}
        <small class="text-error">passwords do not match</small>
      {/if}
    </div>

    <div class="flex justify-center">
      <button
        class="px-4 py-2 text-xl font-bold focus:outline-none focus:ring-black dark:ring-white focus:ring-2 disabled:line-through disabled:cursor-default"
        type="submit"
        disabled={!$isValid}
      >
        sign up
      </button>
    </div>
  </form>
</div>

<Toast />
