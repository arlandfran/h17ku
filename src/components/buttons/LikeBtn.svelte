<script>
  import { csrf, user } from "../../stores";

  export let id;
  export let likesCount;
  export let liked;

  const like = async () => {
    const response = await fetch(`/api/post?id=${id}&like=${!liked}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": $csrf,
      },
      credentials: "same-origin",
      body: JSON.stringify({ username: $user }),
    });

    const result = await response.json();

    if (response.status === 200) {
      liked = result.liked;
      if (liked) {
        likesCount += 1;
        liked = true;
      } else {
        likesCount -= 1;
        liked = false;
      }
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
  };
</script>

<button
  class="flex gap-2 transition btn focus:bg-rose-400 focus:ring-rose-400 hover:bg-rose-400 hover:text-white focus:text-white"
  class:text-rose-500={liked}
  on:click={like}
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
