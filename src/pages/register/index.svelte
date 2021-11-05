<script>
  import { goto } from "@roxi/routify";
  import { createForm } from "svelte-forms-lib";
  import * as yup from "yup";

  let passwordsMatch;

  const { form, errors, isValid, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: "",
      username: "",
      password: "",
      password2: "",
    },
    validationSchema: yup.object().shape({
      email: yup.string().email().required(),
      username: yup
        .string()
        .min(4)
        .trim("no spaces allowed")
        .strict(true)
        .required(),
      password: yup
        .string()
        .min(8)
        .trim("no spaces allowed")
        .strict(true)
        .required(),
      password2: yup
        .string()
        .min(8, "password must be at least 8 characters")
        .trim("no spaces allowed")
        .strict(true)
        .required("confirm password is a required field"),
    }),
    onSubmit: async (values) => {
      if (values.password === values.password2) {
        passwordsMatch = true;

        const postRequest = await fetch("/api/auth/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        });

        const res = await postRequest.json();

        if (postRequest.status === 201) {
          $goto("../login");
        } else if (postRequest.status === 409) {
          if (res.type === "email") {
            $errors.email = res.error;
          } else if (res.type === "username") {
            $errors.username = res.error;
          }
        }
      } else {
        passwordsMatch = false;
      }
    },
  });
</script>

<h1 class="my-4 text-3xl font-bold dark:text-white">create your account</h1>

<div class="w-full max-w-2xl min-w-xs dark:text-white">
  <form on:submit={handleSubmit} class="py-6">
    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> email </label>
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
      <label class="block mb-2 font-bold" for="email"> username </label>
      <input
        class:error={$errors.username}
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="username"
        type="text"
        placeholder="username"
        on:change={handleChange}
        bind:value={$form.username}
      />
      {#if $errors.username}
        <small class="py-2 text-xs text-red-600">{$errors.username}</small>
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

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> confirm password </label>
      <input
        class:error={$errors.password2}
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="password2"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password2}
      />
      {#if $errors.password2}
        <small class="py-2 text-xs text-red-600">{$errors.password2}</small>
      {/if}
      {#if passwordsMatch === false}
        <small class="py-2 text-xs text-red-600">passwords do not match</small>
      {/if}
    </div>

    <div class="flex justify-center">
      <button
        class="px-4 py-2 text-xl font-bold dark:text-white focus:outline-none focus:ring-black dark:ring-white focus:ring-2 disabled:line-through disabled:cursor-default"
        type="submit"
        disabled={!$isValid}
      >
        sign up
      </button>
    </div>
  </form>
</div>

<style>
  .error {
    @apply border border-red-600 ring-red-600;
  }
</style>
