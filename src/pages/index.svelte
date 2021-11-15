<script>
  async function getCurrentTime() {
    const response = await fetch("/api/time");
    const data = await response.json();
    return data.time;
  }

  async function getAllUsers() {
    const response = await fetch("/api/users");
    const data = await response.json();
    return data.users;
  }
</script>

<h1>Routify Starter Template</h1>

<p>
  Go to <a href="/about">/about</a>
</p>

{#await getCurrentTime()}
  The current time is loading...
{:then currentTime}
  The current time is {currentTime}
{/await}

{#await getAllUsers()}
  Loading...
{:then users}
  <h2>Users:</h2>
  {#each users as user}
    <li>{user.username}</li>
  {/each}
{/await}
