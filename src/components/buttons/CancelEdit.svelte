<script>
  export let isEditing;
</script>

<button
  class="transition btn hover:bg-red-600 focus:bg-red-600 focus:ring-red-600 hover:text-white focus:text-white"
  on:click={() => (isEditing = false)}
  ><svg
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
      d="M6 18L18 6M6 6l12 12"
    />
  </svg></button
>
