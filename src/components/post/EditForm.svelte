<script>
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { syllable } from "syllable";
  import { createForm } from "svelte-forms-lib";
  import { haikuSchema } from "../../schemas";
  import { user, csrf } from "../../stores";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";
  import { slide } from "svelte/transition";

  export let _id;
  export let haiku;
  export let isEditing = true;

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
    $form.haiku = haiku;
    document.getElementById("edit-haiku").select();
    count = 17;
  });

  $: count = syllable($form.haiku);

  $: if ($form.haiku.length > 80) {
    $errors.haiku = "you have reached the 80 character limit";
  } else {
    $errors.haiku = "";
  }

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      author: $user,
      haiku: "",
      count: 0,
    },
    validationSchema: haikuSchema,
    onSubmit: async (values) => {
      if (syllable($form.haiku) === 17) {
        const response = await fetch(`/api/post?id=${_id.$oid}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": $csrf,
          },
          credentials: "same-origin",
          body: JSON.stringify(values),
        });

        if (response.status === 200) {
          isEditing = false;
          haiku = $form.haiku;
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

<form on:submit={handleSubmit} id="edit-form">
  <label for="edit" class="sr-only">edit haiku</label>
  <textarea
    name="haiku"
    id="edit-haiku"
    rows="3"
    bind:value={$form.haiku}
    on:change={handleChange}
    class="edit-textarea"
    class:error={$errors.haiku}
  />

  <div class="flex justify-between" in:slide={{ duration: 200 }}>
    <span>
      syllables: {count}
    </span>
    {#if $errors.haiku}
      <span class="text-right">{$errors.haiku}</span>
    {:else if $errors.count}
      <span class="text-right">{$errors.count}</span>
    {/if}
  </div>
</form>

<Toast />
