<script>
  import { onMount } from "svelte";
  import { isAuthenticated } from "../../stores";
  import tippy from "tippy.js";
  import "tippy.js/dist/tippy.css";
  import "tippy.js/themes/translucent.css";

  export let likesCount;
  export let liked;
  export let likeHandler;

  onMount(() => {
    if (!$isAuthenticated) {
      tippy("#like", {
        content: "you must be logged in to like haikus",
        arrow: false,
        hideOnClick: false,
        trigger: "mouseenter focus",
        placement: "bottom-start",
        theme: "translucent",
      });
    }
  });
</script>

{#if $isAuthenticated}
  <button
    class="flex gap-2 transition btn focus:bg-rose-400 focus:ring-rose-400 hover:bg-rose-400 hover:text-white focus:text-white"
    class:text-rose-500={liked}
    on:click={likeHandler}
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="w-6 h-6"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
      />
    </svg>

    {likesCount}
  </button>
{:else}
  <span
    id="like"
    class="rounded-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-black dark:focus-visible:ring-white"
    tabindex="0"
  >
    <button
      class="flex gap-2 disabled:cursor-default btn"
      disabled
      tabindex="-1"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="w-6 h-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
        />
      </svg>

      {likesCount}
    </button>
  </span>
{/if}
