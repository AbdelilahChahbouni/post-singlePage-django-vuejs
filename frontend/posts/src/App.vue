<template>
  <HeaderApp> </HeaderApp>
  <PostApp> </PostApp>
</template>

<script>

import HeaderApp from "./components/HeaderApp.vue";
import PostApp from "./components/PostApp.vue";

export default {
  name: 'App',
  components: {
    HeaderApp,
    PostApp,
  }
}
</script>



