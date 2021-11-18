<script>
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { createForm } from "svelte-forms-lib";
  import { commentSchema } from "../schemas";
  import tippy from "tippy.js";
  import "tippy.js/dist/tippy.css";
  import "tippy.js/themes/translucent.css";
  import { isAuthenticated, user, csrf } from "../stores";

  export let _id;
  export let author;

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
    if (!$isAuthenticated) {
      tippy("#submit", {
        content: "you must be logged in to comment",
        arrow: false,
        hideOnClick: false,
        trigger: "mouseenter focus",
        placement: "bottom-end",
        theme: "translucent",
      });
    }
  });

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      username: $user,
      comment: "",
    },
    validationSchema: commentSchema,
    onSubmit: async (values) => {
      const response = await fetch(`/api/post?id=${_id.$oid}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": $csrf,
        },
        credentials: "same-origin",
        body: JSON.stringify(values),
      });
    },
  });
</script>

<div class="border-b border-black dark:border-gray-400">
  <form class="flex flex-col gap-y-2 my-4" on:submit={handleSubmit}>
    <label for="comment" class="sr-only">reply to {user}:</label>

    <textarea
      name="comment"
      id="comment"
      rows="1"
      class:error={$errors.comment}
      class="textarea"
      placeholder="reply to {author}"
      on:change={handleChange}
      bind:value={$form.comment}
    />

    {#if $errors.comment}
      <span>{$errors.comment}</span>
    {/if}
    {#if $isAuthenticated}
      <button id="submit" class="self-end btn" type="submit"> comment </button>
    {:else}
      <span id="submit" class="self-end btn">
        <button class="line-through cursor-default" disabled> comment </button>
      </span>
    {/if}
  </form>
</div>
