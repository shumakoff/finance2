<template>
  <div class="container-fluid">
    <div class="row">

      <table>
        <tr v-for="record of this.records.result">
          <td>{{ record.date }}</td>
          <td>{{ categories[categories[record.category]['cat']['parent']]['cat']['title'] }} -> {{ categories[record.category]['cat']['title'] }}</td>
          <td>{{ record.item }}</td>
          <td>{{ record.value }}</td>
        </tr>
      </table>

    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  components: {
  },
  props: [],
  data () {
    return {
      records: 0,
      categories: 0,
    }
  },

  mounted() {
    console.log('records mounted');
    this.loadRecords();
    this.loadCategories();
  },

  methods: {

    loadRecords() {
      axios
        .get('/records/')
        .then((response) => { 
          this.records = response.data;
          }
        )
    },

    loadCategories() {
      axios
        .get('/categories/')
        .then((response) => { 
          this.categories = response.data;
          var result = {};
          for (var cat of this.categories) {
            result[cat.id] = {cat};
          }
          this.categories = result;
          console.log(this.categories);
          }
        )
    },

    log(message) {
      console.log(message);
    },

  },

  computed: {

  },
}
</script>

<style>
</style>
