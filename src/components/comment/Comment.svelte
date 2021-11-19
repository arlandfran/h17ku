<script>
  import LikeBtn from "../buttons/LikeBtn.svelte";
  import { onMount, afterUpdate } from "svelte";
  import { getElapsedTime } from "../../helpers";
  import { csrf, user } from "../../stores";

  export let _id;
  export let username;
  export let comment;
  export let posted_at;
  export let likes;

  let time = new Date(posted_at.$date);
  let elapsedTime;
  let liked;
  let likesCount = likes.length;

  onMount(() => {
    elapsedTime = getElapsedTime(time);
  });

  afterUpdate(() => {
    time = new Date(posted_at.$date);
    elapsedTime = getElapsedTime(time);
  });

  const likeHandler = async () => {
    const response = await fetch(`/api/comment?id=${_id.$oid}&like=${!liked}`, {
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
      } else {
        likesCount -= 1;
      }
    } else if (
      response.status === 400 &&
      result.msg === "The CSRF token has expired."
    ) {
      toast.push("session has expired, please refresh the page", {
        initial: 1,
        reversed: true,
        intro: { y: 64 },
      });
    }
  };
</script>

<div
  class="flex flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
>
  <div>
    <span>{username}</span> •
    <time datetime={time.toISOString()}>{elapsedTime}</time>
  </div>
  <p>{comment}</p>

  <div class="flex gap-2 items-center md:gap-4">
    <LikeBtn count={likesCount} {liked} {likeHandler} />
  </div>
</div>
