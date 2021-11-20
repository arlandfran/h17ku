<script>
  import { onMount } from "svelte";
  import { slide } from "svelte/transition";
  import { createForm } from "svelte-forms-lib";
  import { SvelteToast, toast } from "@zerodevx/svelte-toast";
  import { user, csrf, updatePosts } from "../../stores";
  import { haikuSchema } from "../../schemas";
  import { syllable } from "syllable";
  import autosize from "autosize/dist/autosize.min.js";

  export let _id;
  export let haiku;
  export let isEditing;

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
    $form.haiku = haiku;
    document.getElementById("edit-haiku").select();
  });

  $: count = syllable($form.haiku);

  $: if ($form.haiku.length > 80) {
    $errors.haiku = "you have reached the 80 character limit";
  } else {
    $errors.haiku = "";
  }

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      username: $user,
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

        if (response.status === 204) {
          isEditing = false;
          haiku = $form.haiku;
          $updatePosts = true;
        } else if (
          response.status === 400 &&
          result.msg === "The CSRF token has expired."
        ) {
          toast.push("session has expired, please refresh the page", {
            initial: 1,
            duration: 5000,
            reversed: true,
            dismissable: true,
            intro: { y: 64 },
          });
        }
      } else {
        $errors.count = "must be 17 syllables";
      }
    },
  });
</script>

<form on:submit={handleSubmit} id="edit-post-form">
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

<SvelteToast />
