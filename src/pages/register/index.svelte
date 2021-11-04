<script>
  import FormInput from "../../components/FormInput.svelte";
</script>

<h1 class="my-4 text-3xl font-bold dark:text-white">create your account</h1>

<div class="w-full max-w-2xl min-w-xs dark:text-white">
  <form class="py-6">
    <FormInput name="email" label="email" type="email" placeholder="email" />
    <FormInput
      name="user"
      label="username"
      type="text"
      placeholder="username"
    />
    <FormInput
      name="password1"
      label="password"
      type="password"
      placeholder="***********"
    />
    <FormInput
      name="password2"
      label="confirm password"
      type="password"
      placeholder="***********"
    />
    <div class="flex justify-center">
      <button
        class="px-4 py-2 text-2xl font-bold dark:text-white focus:outline-none focus:ring-black dark:ring-white focus:ring-2"
        type="button"
      >
        sign up
      </button>
    </div>
  </form>
</div>
