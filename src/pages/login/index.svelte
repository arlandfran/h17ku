<script>
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  onMount(() => {
    if ($params.newUser) {
      toast.push("new account created!", options);
    }
  });

  const options = {
    initial: 1,
    reversed: true,
    intro: { y: 64 },
    theme: {
      "--toastWidth": "100%",
      "--toastMinHeight": "2rem",
      "--toastPadding": "0 0.5rem",
      "--toastBackground": "#48BB78",
      "--toastBarBackground": "#48BB78",
    },
  };
</script>

<h1 class="text-4xl font-bold dark:text-white">log in</h1>

<Toast />

<style>
  :root {
    --toastContainerTop: auto;
    --toastContainerRight: 1rem;
    --toastContainerBottom: 1rem;
    --toastContainerLeft: 1rem;
  }
</style>
