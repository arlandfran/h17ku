<script>
  import ActionBar from "../components/ActionBar.svelte";
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { syllable } from "syllable";
  import { createForm } from "svelte-forms-lib";
  import { user, csrf, updatePosts } from "../stores";
  import { haikuSchema } from "../schemas";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
    $form.haiku =
      "five syllables here\nseven more syllables here\nfive syllables here";
  });

  $: count = syllable($form.haiku);

  $: if ($form.haiku.length > 80) {
    $errors.haiku = "you have reached the 80 character limit";
  } else {
    $errors.haiku = "";
  }

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      author: "",
      haiku: "",
      count: 0,
    },
    validationSchema: haikuSchema,
    onSubmit: async (values) => {
      $form.author = $user;

      if (syllable($form.haiku) === 17) {
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
          $updatePosts = true;
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
        $errors.count = "must be 17 syllables";
      }
    },
  });
</script>

<div class="flex flex-col gap-2 mb-8 w-full max-w-2xl">
  <form class="flex flex-col gap-2" on:submit={handleSubmit} id="haiku">
    <label for="haiku-validator">compose your haiku:</label>

    <textarea
      id="haiku-validator"
      name="haiku"
      class:error={$errors.haiku || $errors.count}
      class="box-border p-4 w-full whitespace-pre-line rounded border border-black resize-none dark:shadow-lg dark:bg-gray-700 focus:outline-none focus:ring-1 focus:ring-black dark:ring-white dark:border-none dark:focus:ring-2"
      rows="3"
      bind:value={$form.haiku}
      on:change={handleChange}
    />
  </form>

  <div class="flex justify-between">
    <span>
      syllables: {count}
    </span>
    {#if $errors.haiku}
      <span class="text-right">{$errors.haiku}</span>
    {:else if $errors.count}
      <span class="text-right">{$errors.count}</span>
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
