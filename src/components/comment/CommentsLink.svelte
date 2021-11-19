<script>
  import { url } from "@roxi/routify";

  export let id;
  export let username;
  export let comments;
</script>

<div class="flex items-center">
  <a
    href={$url("/:user/:id", { user: username, id: id })}
    class="flex gap-2 transition link hover:bg-blue-600 focus:bg-blue-600 focus:ring-blue-600 hover:text-white focus:text-white"
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
        d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"
      />
    </svg>
    {comments}
  </a>
</div>
