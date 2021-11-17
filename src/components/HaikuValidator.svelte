<script>
  import ActionBar from "../components/ActionBar.svelte";
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { syllable } from "syllable";
  import { createForm } from "svelte-forms-lib";
  import { user, csrf } from "../stores";
  import { haikuSchema } from "../schemas";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
  });

  $: count = syllable($form.haiku);

  $: if ($form.haiku.length > 140) {
    $errors.haiku = "you have reached the 140 character limit";
  } else {
    $errors.haiku = "";
  }

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      author: "",
      haiku: "",
    },
    validationSchema: haikuSchema,
    onSubmit: async (values) => {
      $form.author = $user;

      const response = await fetch("/api/post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": $csrf,
        },
        credentials: "same-origin",
        body: JSON.stringify(values),
      });

      const result = await response.json();

      if (response.status === 200) {
        $form.haiku = "";
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

<div class="flex flex-col gap-2 mb-8 w-full max-w-2xl">
  <form class="flex flex-col gap-2" on:submit={handleSubmit} id="haiku">
    <label for="haiku-validator" class="dark:text-white"
      >compose your haiku:</label
    >

    <textarea
      id="haiku-validator"
      name="haiku"
      class:error={$errors.haiku}
      class="box-border p-4 w-full rounded border border-black resize-none dark:shadow-lg dark:bg-gray-700 dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:ring-white dark:border-none dark:focus:ring-2"
      rows="1"
      placeholder="pineapples are good / apples are very yummy / pen is good i guess"
      bind:value={$form.haiku}
      on:change={handleChange}
    />
  </form>

  <div class="flex justify-between dark:text-white">
    <span>
      syllables: {count}
    </span>
    {#if $errors.haiku}
      <span>{$errors.haiku}</span>
    {/if}
  </div>

  <ActionBar />
</div>

<Toast />

<style>
  .error {
    @apply border border-red-600 ring-red-600;
  }
</style>
