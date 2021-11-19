<script>
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { createForm } from "svelte-forms-lib";
  import { commentSchema } from "../../schemas";
  import tippy from "tippy.js";
  import "tippy.js/dist/tippy.css";
  import "tippy.js/themes/translucent.css";
  import { isAuthenticated, user, csrf, updateComments } from "../../stores";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  export let _id;
  export let username;

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

      if (response.status === 200) {
        $updateComments = true;
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

<div class="border-b border-black dark:border-gray-400">
  <form class="flex flex-col gap-y-2 my-4" on:submit={handleSubmit}>
    <label for="comment" class="sr-only">reply to {user}:</label>

    <textarea
      name="comment"
      id="comment"
      rows="1"
      class:error={$errors.comment}
      class="textarea"
      placeholder="reply to {username}"
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

<Toast />
