<template>
  <main>
    <h1>
      <span>P</span>
      <span>.</span>
      <span>O</span>
      <span>.</span>
      <span>T</span>
    </h1>
    <p>Welcome to POT. This is where you can change the conditions inside your POT and see how your plant is doing.</p>

    <input type="range" name="brightness">
    <label for="brightness"></label>
  </main>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      env_data: {
        
      }
    }
  },
}
</script>