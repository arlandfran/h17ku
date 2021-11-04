<script>
  import { createForm } from "svelte-forms-lib";

  const { form, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: "",
      username: "",
      password: "",
      password2: "",
    },
    onSubmit: (values) => {
      alert(JSON.stringify(values));
    },
  });
</script>

<h1 class="my-4 text-3xl font-bold dark:text-white">create your account</h1>

<div class="w-full max-w-2xl min-w-xs dark:text-white">
  <form on:submit={handleSubmit} class="py-6">
    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> email </label>
      <input
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="email"
        type="email"
        placeholder="email"
        on:change={handleChange}
        bind:value={$form.email}
      />
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> username </label>
      <input
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="username"
        type="text"
        placeholder="username"
        on:change={handleChange}
        bind:value={$form.username}
      />
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> password </label>
      <input
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="password"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password}
      />
    </div>

    <div class="mb-4">
      <label class="block mb-2 font-bold" for="email"> confirm password </label>
      <input
        class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
        id="password2"
        type="password"
        placeholder="**********"
        on:change={handleChange}
        bind:value={$form.password2}
      />
    </div>

    <div class="flex justify-center">
      <button
        class="px-4 py-2 text-xl font-bold dark:text-white focus:outline-none focus:ring-black dark:ring-white focus:ring-2"
        type="submit"
      >
        sign up
      </button>
    </div>
  </form>
</div>
