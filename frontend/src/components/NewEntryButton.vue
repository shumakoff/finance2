<template>
  <a v-on:click="$emit('showentryform')" class="btn btn-primary btn-icon-split">
    <span class="text">New Entry</span>
    <span class="icon text-white-50">
      <font-awesome-icon icon="plus-circle" />
    </span>
  </a>
</template>

<script>

import axios from 'axios';

export default {
  components: {
  },
  data () {
    return {
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
