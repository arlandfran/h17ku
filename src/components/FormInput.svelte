<script>
  export let name;
  export let label;
  export let type;
  export let placeholder;
</script>

<div class="mb-4">
  <label class="block mb-2 font-bold" for={name}> {label} </label>
  <input
    class="px-3 py-2 w-full leading-tight rounded shadow-lg appearance-none focus:outline-none focus:ring-black dark:ring-white focus:ring-2 dark:bg-gray-700"
    id={name}
    {type}
    {placeholder}
  />
</div>
