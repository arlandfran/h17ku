<script>
  import { onMount } from "svelte";
  import { createForm } from "svelte-forms-lib";
  import { SvelteToast, toast } from "@zerodevx/svelte-toast";
  import { csrf, updateComments } from "../../stores";
  import { commentSchema } from "../../schemas";
  import autosize from "autosize/dist/autosize.min.js";

  export let _id;
  export let comment;
  export let isEditing;

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
    $form.comment = comment;
    document.getElementById("edit-comment").select();
  });

  $: if ($form.comment.length > 280) {
    $errors.comment = "you have reached the 280 character limit";
  } else {
    $errors.comment = "";
  }

  const { form, errors, handleChange, handleSubmit } = createForm({
    initialValues: {
      comment: "",
    },
    validationSchema: commentSchema,
    onSubmit: async (values) => {
      const response = await fetch(`/api/comment?id=${_id.$oid}`, {
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
        comment = $form.comment;
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

<form on:submit={handleSubmit} id="edit-comment-form">
  <label for="edit" class="sr-only">edit comment</label>
  <textarea
    name="comment"
    id="edit-comment"
    rows="1"
    bind:value={$form.comment}
    on:change={handleChange}
    class="box-border p-4 w-full whitespace-pre-line resize-none dark:bg-gray-800 focus:outline-none"
    class:error={$errors.comment}
  />

  {#if $errors.comment}
    <span class="text-right">{$errors.comment}</span>
  {:else if $errors.count}
    <span class="text-right">{$errors.count}</span>
  {/if}
</form>

<SvelteToast />
