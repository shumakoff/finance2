<template>

  <!--<p>This component’s code is in {{ filename }}</p>-->
  <Content>
  </Content>

</template>

<script>
import axios from 'axios';
import Content from './components/Content.vue'

export default {
  name: 'app',
  components: {
    'Content': Content,
  },
  data () {
    return {
      filename: 'App.vue',
    }
  },
  methods: {

  },

  computed: {

  },
}
</script>

<style>
</style>
